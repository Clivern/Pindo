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




import docker

if __name__ == '__main__':
    client = docker.from_env()

    container = client.containers.run(
        "python:3.9",
        "bash /code/exec.sh",
        volumes={'/etc/pindo/46da9ee8-55a3-4d5a-9ade-4c3f3047321f': {'bind': '/code', 'mode': 'rw'}},
        detach=True
    )

    result = []
    for line in container.logs(stream=True):
        result.append(str(line, 'utf-8'))

    print("".join(result))

    client.api.remove_container(container.id, force=True, v=True)