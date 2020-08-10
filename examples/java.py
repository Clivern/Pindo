from pindo.runner import Runner

if __name__ == "__main__":

	code = """
	public class HelloWorld{

	     public static void main(String []args){
	        System.out.println("Hello World");
	     }
	}
	"""

	java_code = Runner.java(code, "17.0", None, {"main_class": "HelloWorld"})

	engine = Runner.docker("/etc/pindo", java_code)

	engine.setup()
	print(engine.run())
	engine.cleanup()
