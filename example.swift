// this is a single line comment using two slashes.

// Swift variables are declared with "var"
// this is followed by a name, a type, and a value
var explicitDouble: Double = 70

// If the type is omitted, Swift will infer it from
// the variable's initial value
var implicitInteger = 70
var implicitDouble = 70.0
var 國 = "美國"

// Swift constants are declared with "let"
// followed by a name, a type, and a value
let numberOfBananas: Int = 10

// Like variables, if the type of a constant is omitted,
// Swift will infer it from the constant's value
let numberOfApples = 3
let numberOfOranges = 5

// Values of variables and constants can both be
// interpolated in strings as follows
let appleSummary = "I have \(numberOfApples) apples."
let fruitSummary = "I have \(numberOfApples + numberOfOranges) pieces of fruit."

// In "playgrounds", code can be placed in the global scope
println("Hello, world")

// This is an array variable
var fruits = ["mango", "kiwi", "avocado"]

// Define a dictionary with four items:
// Each item has a person's name and age
let people = ["Anna": 67, "Beto": 8, "Jack": 33, "Sam": 25]

// Functions and methods are both declared with the
// "func" syntax, and the return type is specified with ->
func sayHello(personName: String) -> String {
    let greeting = "Hello, " + personName + "!"
    return greeting
}

// prints "Hello, Dilan!"
print(sayHello("Dilan"))

// Parameter names can be made external and required
// for calling.
// The external name can be the same as the parameter
// name by prefixing with an octothorpe (#)
// - or it can be defined separately.

func sayAge(#personName: String, personAge age: Int) -> String {
    let result = "\(personName) is \(age) years old."
    return result
}

sayAge(personName:"Jaden", personAge:19)

// We can also specify the name of the parameter

print(sayAge(personName: "Dilan", personAge: 42))
