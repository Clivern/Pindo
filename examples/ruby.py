from pindo.runner import Runner

if __name__ == "__main__":

	code = "puts 'Hello World'"

	ruby_code = Runner.ruby(code, "3.0.0")

	engine = Runner.docker("/etc/pindo", ruby_code)

	engine.setup()
	print(engine.run())
	engine.cleanup()
