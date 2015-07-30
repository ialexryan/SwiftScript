import re

def remove_substrings(line, spans):
    num_removed_chars = 0
    for span in spans:
        start = span[0] - num_removed_chars
        end = span[1] - num_removed_chars
        line = line[:start] + line[end:]
        num_removed_chars += (span[1] - span[0])
    return line

transformations = []

def trans1(line):
    return line.replace("let", "const")
transformations.append(trans1)

def trans2(line):
    return line.replace("println", "console.log").replace("print", "console.log")
transformations.append(trans2)

def trans3(line):
    return line.replace(" -> ", ": ")
transformations.append(trans3)

def trans4(line):
    return line.replace(": Bool", ": boolean")
transformations.append(trans4)

def trans5(line):
    return line.replace(": String", ": string")
transformations.append(trans5)

def trans6(line):
    return line.replace(": Int", ": number")
transformations.append(trans6)

def trans7(line):
    return line.replace(": Float", ": number")
transformations.append(trans7)

def trans8(line):
    return line.replace(": Double", ": number")
transformations.append(trans8)

# Transform function definitions
def trans9(line):
    p = re.compile(r'func (\w\S*) ?\((.*)\)(.*)')
    # This regex returns three groups, the first is the function name
    #  and the second is the arguments and the third is the type and etc.
    m = p.search(line)
    if m:
        name = m.group(1)
        args = m.group(2)
        type = m.group(3)
        namedArguments = False
        for arg in args.split(", "):
            if arg[0] == "#" or len(arg.split(" ")) == 3:
                namedArguments = True
        if namedArguments:
            a = ""
            restore = ""
            for arg in args.split(", "):
                if arg[0] == "#":
                    arg = arg[1:]
                    arg_name = arg.split(":")[0]
                    a += arg + ", "
                    restore += "    var " + arg_name + " = a." + arg_name + ";\n"
                elif len(arg.split(" ")) == 3:
                    arg = arg.replace(":", "")
                    arg = arg.split(" ")
                    arg_external_name = arg[0]
                    arg_internal_name = arg[1]
                    arg_type = arg[2]
                    a += arg_external_name + ": " + arg_type + ", "
                    restore += "    var " + arg_internal_name + " = a." + arg_external_name + ";\n"
            a = a[:-2]  #remove trailing ,
            return line.replace(m.group(0), "function " + name + "(a: {" + a + "})" + type) + restore
        else:
            return line.replace("func ", "function ")
    else:
        return line
transformations.append(trans9)

# Transform function calls
def trans10(line):
    if "function" in line:
        return line
    else:
        p = re.compile(r'(console.log\()(.*)(\))')
        m = p.search(line)
        if m:
            target = remove_substrings(line, [m.span(1), m.span(3)])
        else:
            target = line
        p = re.compile(r'(\w\S*) ?\((.*)\)')
        # This regex matches a function call and returns two groups,
        #  the function name and the list of arguments
        m = p.search(target)
        if m:
            name = m.group(1)
            args = m.group(2)
            if ":" in args:
                return line.replace(m.group(0), name + "({" + args + "})")
            else:
                return line
        else:
            return line
transformations.append(trans10)

# Replace format strings
def trans11(line):
    p = re.compile(r'["`](.*)\\\((.*)\)(.*)["`]')
    m = p.search(line)
    if m:
        return trans11(line.replace(m.group(0), "`" + m.group(1) + "${" + m.group(2) + "}" + m.group(3) + "`"))
    else:
        return line
transformations.append(trans11)

# Add semicolons
def trans12(line):
    if line.strip().endswith("{") or line.strip().endswith("}") or line.strip().endswith(";") or line == "\n":
        return line
    else:
        return line[:-1] + ";\n"
transformations.append(trans12)

# Turn dictionaries into objects
def trans13(line):
    p = re.compile(r'\[(.*:.*)\]')
    m = p.search(line)
    if m:
        return line.replace(m.group(0), "{" + m.group(1) + "}")
    else:
        return line
transformations.append(trans13)
