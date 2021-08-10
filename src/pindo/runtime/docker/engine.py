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
from .c import C
from .go import Go
from .php import PHP
from .rust import Rust
from .ruby import Ruby
from .java import Java
from .cplus import Cplus
from .python import Python
from pindo.lang import Lang
from pindo.exception.code_failed_to_run import CodeFailedToRun


class Engine():
    """Docker Engine"""

    def __init__(self, code, docker_client=None):
        self._code = code
        self._runtime = Engine.get_runtime(code)
        self._docker_client = docker.from_env() if docker_client is None else docker_client

    def run(self, configs={}):
        """
        Execute the code on docker

        Returns:
            The output, execution and build time
        """
        defaults = {
            "mount_mode": "ro",
            "mem_limit": "100m",
            "cpu_period": 100000,
            "cpu_quota": 50000
        }

        defaults.update(configs)

        try:
            if "runtime" in defaults.keys():
                # Run container in background using a different runtime
                # like gvisor https://github.com/google/gvisor for better isolation
                container = self._docker_client.containers.run(
                    "{}:{}".format(self._runtime.image, self._runtime.version),
                    "bash /code/exec.sh",
                    name=self._code.id,
                    volumes={self._code.id: {'bind': '/code', 'mode': defaults["mount_mode"]}},
                    detach=True,
                    mem_limit=defaults["mem_limit"],
                    cpu_period=defaults["cpu_period"],
                    cpu_quota=defaults["cpu_quota"],
                    runtime=defaults["runtime"]
                )
            else:
                # Run container in background using the default runtime
                container = self._docker_client.containers.run(
                    "{}:{}".format(self._runtime.image, self._runtime.version),
                    "bash /code/exec.sh",
                    name=self._code.id,
                    volumes={self._code.id: {'bind': '/code', 'mode': defaults["mount_mode"]}},
                    detach=True,
                    mem_limit=defaults["mem_limit"],
                    cpu_period=defaults["cpu_period"],
                    cpu_quota=defaults["cpu_quota"]
                )
        except Exception as e:
            raise CodeFailedToRun("Code %s failed to run: {}".format(self._code.id, str(e)))

        result = []

        for line in container.logs(stream=True):
            result.append(str(line, 'utf-8'))

        result = "".join(result)
        items = result.rsplit("-------", 1)
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
        Create an executable script on a docker volume
        """
        try:
            volume = self._docker_client.volumes.create(
                name=self._code.id,
                driver='local'
            )

            file = "{}/{}".format(volume.attrs['Mountpoint'], "exec.sh")

            if self._code.lang == Lang.JAVA:
                # Java Script
                script = "{}/{}.{}".format(
                    volume.attrs['Mountpoint'],
                    self._runtime.main_class,
                    self._runtime.extension
                )
            else:
                # Other Scripts
                script = "{}/run.{}".format(
                    volume.attrs['Mountpoint'],
                    self._runtime.extension
                )

            f = open(file, "w")
            f.write(self._runtime.script)
            f.close()

            f = open(script, "w")
            f.write(self._code.code)
            f.close()

        except Exception as e:
            raise Exception("Error while creating volume: {}".format(str(e)))

    def cleanup(self):
        """
        Removes the code volume
        """
        try:
            container = self._docker_client.containers.get(self._code.id)

            if container:
                self._docker_client.api.remove_container(container.id, force=True, v=True)

            volume = self._docker_client.volumes.get(self._code.id)

            if volume:
                volume.remove(force=True)

        except Exception as e:
            raise Exception("Error while removing the volume: {}".format(str(e)))

    @property
    def code(self):
        """
        Returns:
            The code instance
        """
        return self._code

    @property
    def runtime(self):
        """
        Returns:
            The runtime instance
        """
        return self._runtime

    @property
    def docker_client(self):
        """
        Returns:
            The docker client
        """
        return self._docker_client

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

        elif code.lang == Lang.CPLUS:
            return Cplus(code.version)

        elif code.lang == Lang.C:
            return C(code.version)

        elif code.lang == Lang.JAVA:
            if "main_class" in code.meta.keys():
                main_class = code.meta["main_class"]
            else:
                main_class = "Main"

            return Java(code.version, main_class)

        elif code.lang == Lang.RUBY:
            return Ruby(code.version)

        else:
            raise Exception("Invalid language {}".format(self._code.lang.value))
