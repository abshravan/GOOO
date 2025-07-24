package main

import "fmt"

func main() {
	// --- Basic Data Types ---

	// Booleans
	var isGoFun bool = true
	fmt.Println("Boolean (isGoFun):", isGoFun)

	// Numeric Types

	// Integers (signed and unsigned)
	var age int = 30 // int is typically 32 or 64 bits depending on the system
	fmt.Println("Integer (age):", age)

	var bigInt int64 = 9223372036854775807 // Max value for int64
	fmt.Println("int64 (bigInt):", bigInt)

	var smallUint uint8 = 255 // Max value for uint8 (0 to 255)
	fmt.Println("uint8 (smallUint):", smallUint)

	// Floating-point numbers
	var price float32 = 19.99
	fmt.Println("Float32 (price):", price)

	var pi float64 = 3.1415926535
	fmt.Println("Float64 (pi):", pi)

	// Complex numbers
	var complexNum complex64 = 1 + 2i // complex64 uses float32 real and imaginary parts
	fmt.Println("Complex64 (complexNum):", complexNum)

	var anotherComplex complex128 = 3.5 + 4.8i // complex128 uses float64 real and imaginary parts
	fmt.Println("Complex128 (anotherComplex):", anotherComplex)

	// Strings
	var greeting string = "Hello, Go!"
	fmt.Println("String (greeting):", greeting)

	var multiLineString string = `This is a
multi-line
string.`
	fmt.Println("Multi-line String:", multiLineString)

	// --- Composite Data Types ---

	// Arrays (fixed-size collection of elements of the same type)
	var numbers [3]int = [3]int{10, 20, 30}
	fmt.Println("Array (numbers):", numbers)
	fmt.Println("First element of array:", numbers[0])

	// Slices (dynamic-size, flexible view into an array)
	var fruits []string = []string{"apple", "banana", "cherry"}
	fmt.Println("Slice (fruits):", fruits)
	fruits = append(fruits, "date") // Slices can grow
	fmt.Println("Slice after append:", fruits)

	// Maps (unordered collection of key-value pairs)
	var ages map[string]int = map[string]int{
		"Alice": 25,
		"Bob":   30,
	}
	fmt.Println("Map (ages):", ages)
	fmt.Println("Bob's age:", ages["Bob"])
	ages["Charlie"] = 35 // Add a new entry
	fmt.Println("Map after adding Charlie:", ages)

	// Structs (custom aggregate type that groups together related fields)
	type Person struct {
		Name string
		Age  int
		City string
	}
	var p1 Person = Person{Name: "Eve", Age: 28, City: "New York"}
	fmt.Println("Struct (p1):", p1)
	fmt.Println("Person's name:", p1.Name)

	// --- Pointer Type ---
	var x int = 10
	var ptr *int = &x // ptr now holds the memory address of x
	fmt.Println("Integer (x):", x)
	fmt.Println("Pointer (ptr - memory address of x):", ptr)
	fmt.Println("Value at pointer (dereferencing ptr):", *ptr) // Dereferencing to get the value

	*ptr = 20 // Change value of x through the pointer
	fmt.Println("Integer (x) after pointer modification:", x)

	// --- Nil values for reference types ---
	var nilSlice []int
	var nilMap map[string]string
	var nilPointer *int
	// fmt.Println("Nil Slice:", nilSlice) // Printing nil values might show empty brackets or map{}
	// fmt.Println("Nil Map:", nilMap)
	// fmt.Println("Nil Pointer:", nilPointer)

	if nilSlice == nil {
		fmt.Println("nilSlice is nil")
	}
	if nilMap == nil {
		fmt.Println("nilMap is nil")
	}
	if nilPointer == nil {
		fmt.Println("nilPointer is nil")
	}
}
