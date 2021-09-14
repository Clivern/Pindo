# MIT License
#
# Copyright (c) 2021 Clivern
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import stat
import docker
import shutil
from .go import Go
from .php import PHP
from .rust import Rust
from .ruby import Ruby
from .java import Java
from .mysql import MySQL
from .python import Python
from pindo.lang import Lang
from pindo.exception.code_failed_to_run import CodeFailedToRun


class Engine():
    """Docker Engine"""

    def __init__(self, local_storage_path, code, docker_client=None):
        self._code = code
        self._runtime = Engine.get_runtime(code)
        self._local_storage_path = local_storage_path.rstrip("/")
        self._docker_client = docker.from_env() if docker_client is None else docker_client

    def run(self):
        """
        Execute the code on docker

        Returns:
            The output, execution and build time
        """
        try:
            result = self._docker_client.containers.run(
                "{}:{}".format(self._runtime.image, self._runtime.version),
                "bash /code/exec.sh",
                volumes={"{}/{}".format(self._local_storage_path, self._code.id): {'bind': '/code', 'mode': 'rw'}}
            )
        except Exception as e:
            raise CodeFailedToRun("Code %s failed to run: {}".format(self._code.id, str(e)))

        items = str(result).rsplit("-------", 1)
        stats = items[1].split("\n")
        build_time = None
        execution_time = None

        for x in range(len(stats)):
            if "Build time in milliseconds: " in stats[x]:
                build_time = stats[x].replace("Build time in milliseconds: ", "")
            if "Execution time in milliseconds: " in stats[x]:
                execution_time = stats[x].replace("Execution time in milliseconds: ", "")

        return {
            "output": items[0],
            "build_time": build_time,
            "execution_time": execution_time,
        }

    def setup(self):
        """
        Create an executable script on local host
        """
        path = "{}/{}".format(self._local_storage_path, self._code.id)
        file = "{}/{}".format(path, "exec.sh")
        script = "{}/run.{}".format(path, self._runtime.extension)

        if not os.path.isdir(path):
            os.makedirs(path)

        f = open(file, "w")
        f.write(self._runtime.script)
        f.close()

        f = open(script, "w")
        f.write(self._code.code)
        f.close()

        st = os.stat(file)
        os.chmod(file, st.st_mode | stat.S_IEXEC)

    def cleanup(self):
        """
        Remove code dir
        """
        path = "{}/{}".format(self._local_storage_path, self._code.id)
        shutil.rmtree(path)

    @classmethod
    def get_runtime(cls, code):
        """
        Build Runtime from code data

        Args:
            code: an instance of code class

        Returns:
            an instance of the right runtime
        """
        if code.lang == Lang.RUST:
            return Rust(code.version)

        elif code.lang == Lang.GO:
            return Go(code.version)

        elif code.lang == Lang.PHP:
            return PHP(code.version)

        elif code.lang == Lang.PYTHON:
            return Python(code.version)

        elif code.lang == Lang.JAVA:
            if "main_class" in code.meta.keys():
                main_class = code.meta["main_class"]
            else:
                main_class = "Run"

            return Java(code.version, main_class)

        elif code.lang == Lang.RUBY:
            return Ruby(code.version)

        elif code.lang == Lang.MYSQL:
            return MySQL(code.version)

        else:
            raise Exception("Invalid language {}".format(self._code.lang.value))
