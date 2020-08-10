from pindo.runner import Runner

if __name__ == "__main__":

    code = """
    fn main() {
        println!("Hello, world!");
    }
    """

    rust_code = Runner.rust(code, "1.57.0")

    engine = Runner.docker("/etc/pindo", rust_code)

    engine.setup()
    print(engine.run())
    engine.cleanup()
