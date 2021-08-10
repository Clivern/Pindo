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

from .code import Code
from .lang import Lang
from .runtime.docker.c import C
from .runtime.docker.go import Go
from .runtime.docker.php import PHP
from .runtime.docker.rust import Rust
from .runtime.docker.ruby import Ruby
from .runtime.docker.java import Java
from .runtime.docker.cplus import Cplus
from .runtime.docker.python import Python
from .runtime.docker.engine import Engine
from .exception.invalid_runtime_version import InvalidRuntimeVersion


class Runner():
    """Factory Class for Runtime engine and Programming Languages Supported"""

    @classmethod
    def docker(cls, code, docker_client=None):
        """
        Get an instance of docker engine

        Args:
            code: an instance of Code class with the code snippet, language and version
            docker_client: an instance of docker client

        Returns:
            an instance of docker engine
        """
        if not code or not isinstance(code, Code):
            raise Exception("Code of type Code must be provided!")

        return Engine(code, docker_client)

    @classmethod
    def go(cls, code, version, id=None, meta={}):
        """
        Get an instance of go runtime

        Args:
            code: the code snippet to run
            version: the language version
            id: code item uuid
            meta: meta data that may be needed for the runtime

        Returns:
            an instance of Code class
        """
        if version not in Go().versions.keys():
            raise InvalidRuntimeVersion("Invalid version {} for runtime {}".format(
                version,
                Lang.GO.value
            ))

        return Code(code, Lang.GO, version, id, meta)

    @classmethod
    def php(cls, code, version, id=None, meta={}):
        """
        Get an instance of php runtime

        Args:
            code: the code snippet to run
            version: the language version
            id: code item uuid
            meta: meta data that may be needed for the runtime

        Returns:
            an instance of Code class
        """
        if version not in PHP().versions.keys():
            raise InvalidRuntimeVersion("Invalid version {} for runtime {}".format(
                version,
                Lang.PHP.value
            ))

        return Code(code, Lang.PHP, version, id, meta)

    @classmethod
    def ruby(cls, code, version, id=None, meta={}):
        """
        Get an instance of ruby runtime

        Args:
            code: the code snippet to run
            version: the language version
            id: code item uuid
            meta: meta data that may be needed for the runtime

        Returns:
            an instance of Code class
        """
        if version not in Ruby().versions.keys():
            raise InvalidRuntimeVersion("Invalid version {} for runtime {}".format(
                version,
                Lang.RUBY.value
            ))

        return Code(code, Lang.RUBY, version, id, meta)

    @classmethod
    def java(cls, code, version, id=None, meta={}):
        """
        Get an instance of java runtime

        Args:
            code: the code snippet to run
            version: the language version
            id: code item uuid
            meta: meta data that may be needed for the runtime

        Returns:
            an instance of Code class
        """
        if version not in Java().versions.keys():
            raise InvalidRuntimeVersion("Invalid version {} for runtime {}".format(
                version,
                Lang.JAVA.value
            ))

        return Code(code, Lang.JAVA, version, id, meta)

    @classmethod
    def python(cls, code, version, id=None, meta={}):
        """
        Get an instance of python runtime

        Args:
            code: the code snippet to run
            version: the language version
            id: code item uuid
            meta: meta data that may be needed for the runtime

        Returns:
            an instance of Code class
        """
        if version not in Python().versions.keys():
            raise InvalidRuntimeVersion("Invalid version {} for runtime {}".format(
                version,
                Lang.PYTHON.value
            ))

        return Code(code, Lang.PYTHON, version, id, meta)

    @classmethod
    def rust(cls, code, version, id=None, meta={}):
        """
        Get an instance of rust runtime

        Args:
            code: the code snippet to run
            version: the language version
            id: code item uuid
            meta: meta data that may be needed for the runtime

        Returns:
            an instance of Code class
        """
        if version not in Rust().versions.keys():
            raise InvalidRuntimeVersion("Invalid version {} for runtime {}".format(
                version,
                Lang.RUST.value
            ))

        return Code(code, Lang.RUST, version, id, meta)

    @classmethod
    def c(cls, code, version, id=None, meta={}):
        """
        Get an instance of C runtime

        Args:
            code: the code snippet to run
            version: the language version
            id: code item uuid
            meta: meta data that may be needed for the runtime

        Returns:
            an instance of Code class
        """
        if version not in C().versions.keys():
            raise InvalidRuntimeVersion("Invalid version {} for runtime {}".format(
                version,
                Lang.C.value
            ))

        return Code(code, Lang.C, version, id, meta)

    @classmethod
    def cplus(cls, code, version, id=None, meta={}):
        """
        Get an instance of C++ runtime

        Args:
            code: the code snippet to run
            version: the language version
            id: code item uuid
            meta: meta data that may be needed for the runtime

        Returns:
            an instance of Code class
        """
        if version not in Cplus().versions.keys():
            raise InvalidRuntimeVersion("Invalid version {} for runtime {}".format(
                version,
                Lang.CPLUS.value
            ))

        return Code(code, Lang.CPLUS, version, id, meta)
