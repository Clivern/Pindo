from pindo.runner import Runner

if __name__ == "__main__":

	code = """
	// You can edit this code!
	// Click here and start typing.
	package main

	import "fmt"

	func main() {
		fmt.Println("Hello, 世界")
	}
	"""

	go_code = Runner.go(code, "1.17")

	engine = Runner.docker("/etc/pindo", go_code)

	engine.setup()
	print(engine.run())
	engine.cleanup()
