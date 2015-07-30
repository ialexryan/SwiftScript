#!/usr/bin/python

import sys, os, argparse
from subprocess import call
from transformations import transformations

__author__ = 'Alex Ryan'


# Check for command-line options
# --toJS runs through tsc at the end
def get_CL_args():
    parser = argparse.ArgumentParser(description='SwiftScript converts a subset of Swift to TypeScript.')
    parser.add_argument('-j','--toJS', help='Postprocess with TypeScript compiler', required=False, action='store_true')
    parser.add_argument('input_filename', help="Input filename", nargs=1)
    args = parser.parse_args()
    return args


def transform_line(line):
    # Ignore comments
    if line.startswith("//"):
        return line
    # Apply our syntax transformations, one line at a time
    for trans in transformations:
        line = trans(line)
    return line


# Run the transformations on every line of a file, and write the output
def transform_file(name):
    output = ""
    output_name = name + ".ts"
    with open(name, 'r') as f:
        for line in f:
            output += transform_line(line)
    with open(output_name, 'w') as f:
        f.write(output)
    print ""
    print "    Swift to TypeScript transformation complete!"
    print "    Remember to check the TypeScript file for correctness."
    print ""


def invokeTSC(name):
    if call(["which", "tsc"], stdout=open(os.devnull, 'w')):
        # `which tsc` returned non-zero exit code
        print ""
        print "    tsc not found - install typescript to use the --toJS option."
        print "    Try sudo npm install -g typescript"
        print ""
    else:
        # `which tsc` returned zero -> safe to call tsc
        print ""
        print "    Beginning TypeScript compilation..."
        call(["tsc", name + ".ts"])


def main():
    args = get_CL_args()

    transform_file(args.input_filename[0])

    if args.toJS:
        invokeTSC(args.input_filename[0])

if __name__ == "__main__":
    main()
