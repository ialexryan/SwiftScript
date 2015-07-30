func test(cat: String, dog: String) -> String {
    println("Hello \(cat) world")
    return dog
}

var a = func test2(#cat: String, canine dog: String) -> String {
    return cat + dog
}

let x = 5
let y = 10.5
let s: String = "Hello \(x+y) world"

var q = test("binx", "fido")

var r = a(cat: "bijou", canine: s)
