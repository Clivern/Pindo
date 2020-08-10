from pindo.runner import Runner

if __name__ == "__main__":

	code = "print('Hello World')"

	python_code = Runner.python(code, "3.9")

	engine = Runner.docker("/etc/pindo", python_code)

	engine.setup()
	print(engine.run())
	engine.cleanup()
