from pindo.runner import Runner

if __name__ == "__main__":

	code = """
	<?php
	echo "Hello World";
	"""

	php_code = Runner.php(code, "7.4")

	engine = Runner.docker("/etc/pindo", php_code)

	engine.setup()
	print(engine.run())
	engine.cleanup()
