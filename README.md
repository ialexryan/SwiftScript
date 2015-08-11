# SwiftScript

## Usage:

`./swiftscript.py example.swift` will output `example.swift.ts`.

`./swiftscript.py --toJS example.swift` will output `example.swift.ts` and attempt to run `example.swift.ts` through the TypeScript compiler, outputting `example.swift.js`.

WARNING: SwiftScript is not smart enough to make sure that it always outputs valid TypeScript! (It's literally just a few regular expressions. For now, garbage in -> garbage out :)

## About:

A Swift-to-JavaScript compiler would be pretty cool, since it would allow development for mobile, desktop, and web in one language. Fortunately the [TypeScript](http://www.typescriptlang.org) folks have done almost all of the hard work, and conveniently (a limited subset of) Swift can be converted to TypeScript with nothing but syntax transformations.

This project tries to be an easy-to-understand and easy-to-use tool for **writing TypeScript in Swift syntax**. I don't currently plan to add support for all of Swift's long list of advanced features, but we'll see how far it goes.

Below are the syntax transformations that will be supported, with Swift code on the first line and the equivalent TypeScript code on the second.

---

```Swift
let x = 5
```
```TypeScript
const x = 5;
```

---

```Swift
println("Hello")
```
```TypeScript
console.log("Hello");
```

---

```Swift
func test(cat: String, dog: String) -> String {}
test("binx", "fido")
```
```TypeScript
function test(cat: string, dog: string): string {}
test("binx", "fido");
```

---

```Swift
func test(#cat: String, canine dog: String) -> String {
    return dog + cat
}
test(cat: "bijou", canine: "fido")
```

```TypeScript
function test(args: {cat: string, canine: string}): string {
    var cat = args.cat;
    var dog = args.canine;
    return dog + cat;
}
test({cat: "binx", canine: "fido"})
```

---

```Swift
"Hello \(a+b) world"
```

```TypeScript
`Hello ${a+b} world`
```

---

`Bool` maps to `boolean`, `String` maps to `string`, and `Int`/`Float`/`Double` map to `number`.

---

## Todo:

- if/else statements
- for/while loops


## Wishlist:

- variadic functions
- optional arguments
- parameter default values
- `var [x,y] = [10,20]`
- structs to interfaces
- classes to classes
- lambdas
