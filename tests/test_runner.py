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

import pytest

from pindo.code import Code
from pindo.lang import Lang
from pindo.runner import Runner
from pindo.runtime.docker.engine import Engine
from pindo.exception.invalid_runtime_version import InvalidRuntimeVersion


def test_runner():
    """Runner Tests"""
    ruby_code = Runner.ruby("~~", "3.0.0")
    php_code = Runner.php("~~", "8.1")
    python_code = Runner.python("~~", "3.9")
    go_code = Runner.go("~~", "1.17")
    rust_code = Runner.rust("~~", "1.57.0")
    java_code = Runner.java("~~", "17.0")

    assert isinstance(ruby_code, Code) == True
    assert isinstance(php_code, Code) == True
    assert isinstance(python_code, Code) == True
    assert isinstance(go_code, Code) == True
    assert isinstance(rust_code, Code) == True
    assert isinstance(java_code, Code) == True

    # Invalid Version
    with pytest.raises(InvalidRuntimeVersion):
        Runner.ruby("~~", "1.0.0")

    with pytest.raises(InvalidRuntimeVersion):
        Runner.php("~~", "1.0.0")

    with pytest.raises(InvalidRuntimeVersion):
        Runner.python("~~", "1.0.0")

    with pytest.raises(InvalidRuntimeVersion):
        Runner.go("~~", "1.0.0")

    with pytest.raises(InvalidRuntimeVersion):
        Runner.rust("~~", "1.0.0")

    with pytest.raises(InvalidRuntimeVersion):
        Runner.java("~~", "1.0.0")

    # Invalid Code
    with pytest.raises(Exception):
        Runner.docker("", "~")

    assert isinstance(Runner.docker(ruby_code, "~"), Engine) == True
