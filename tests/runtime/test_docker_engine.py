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
import pytest
from unittest.mock import Mock
from pindo.runner import Runner
from pindo.runner import Runner
from pindo.runtime.docker.go import Go
from pindo.runtime.docker.java import Java
from pindo.runtime.docker.mysql import MySQL
from pindo.runtime.docker.php import PHP
from pindo.runtime.docker.python import Python
from pindo.runtime.docker.ruby import Ruby
from pindo.runtime.docker.rust import Rust
from pindo.runtime.docker.engine import Engine


def test_docker_engine():
    docker = Mock()
    docker.containers.run.return_value = "Hello World\n-------\nBuild time in milliseconds: 20\nExecution time in milliseconds: 60\n"

    path = os.path.dirname(os.path.realpath(__file__)) + "/../../cache"
    code = Runner.ruby("puts 'Hello World'", "3.0.0")
    engine = Engine(path, code, docker)

    engine.setup()
    assert os.path.isfile("{}/{}/run.rb".format(path, code.id)) == True
    assert os.path.isfile("{}/{}/exec.sh".format(path, code.id)) == True

    assert engine.run() == {'build_time': '20', 'execution_time': '60', 'output': 'Hello World\n'}

    engine.cleanup()
    assert os.path.isfile("{}/{}/run.rb".format(path, code.id)) == False
    assert os.path.isfile("{}/{}/exec.sh".format(path, code.id)) == False

    ruby_code = Runner.ruby("~~", "3.0.0")
    php_code = Runner.php("~~", "8.1")
    python_code = Runner.python("~~", "3.9")
    go_code = Runner.go("~~", "1.17")
    rust_code = Runner.rust("~~", "1.57.0")
    java_code = Runner.java("~~", "17.0")
    mysql_code = Runner.mysql("~~", "8.0")

    assert isinstance(Engine.get_runtime(ruby_code), Ruby) == True
    assert isinstance(Engine.get_runtime(php_code), PHP) == True
    assert isinstance(Engine.get_runtime(python_code), Python) == True
    assert isinstance(Engine.get_runtime(go_code), Go) == True
    assert isinstance(Engine.get_runtime(rust_code), Rust) == True
    assert isinstance(Engine.get_runtime(java_code), Java) == True
    assert isinstance(Engine.get_runtime(mysql_code), MySQL) == True
