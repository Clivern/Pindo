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

from pindo.runtime.docker.go import Go
from pindo.runtime.docker.java import Java
from pindo.runtime.docker.php import PHP
from pindo.runtime.docker.python import Python
from pindo.runtime.docker.ruby import Ruby
from pindo.runtime.docker.rust import Rust


def test_go_runtime():
    """Go Runtime Tests"""
    go_rt = Go("1.0.0")

    assert isinstance(go_rt, Go) == True
    assert go_rt.script != ""
    assert "#!/bin/bash" in go_rt.script
    assert isinstance(go_rt.versions, dict) == True
    assert len(go_rt.versions) > 0
    assert go_rt.image != ""
    assert go_rt.extension != ""
    assert go_rt.version == "1.0.0"


def test_java_runtime():
    """Java Runtime Tests"""
    java_rt = Java("1.0.0")

    assert isinstance(java_rt, Java) == True
    assert java_rt.script != ""
    assert "#!/bin/bash" in java_rt.script
    assert isinstance(java_rt.versions, dict) == True
    assert len(java_rt.versions) > 0
    assert java_rt.image != ""
    assert java_rt.extension != ""
    assert java_rt.version == "1.0.0"
    assert java_rt.main_class == "Run"


def test_php_runtime():
    """PHP Runtime Tests"""
    php_rt = PHP("1.0.0")

    assert isinstance(php_rt, PHP) == True
    assert php_rt.script != ""
    assert "#!/bin/bash" in php_rt.script
    assert isinstance(php_rt.versions, dict) == True
    assert len(php_rt.versions) > 0
    assert php_rt.image != ""
    assert php_rt.extension != ""
    assert php_rt.version == "1.0.0"


def test_python_runtime():
    """Python Runtime Tests"""
    python_rt = Python("1.0.0")

    assert isinstance(python_rt, Python) == True
    assert python_rt.script != ""
    assert "#!/bin/bash" in python_rt.script
    assert isinstance(python_rt.versions, dict) == True
    assert len(python_rt.versions) > 0
    assert python_rt.image != ""
    assert python_rt.extension != ""
    assert python_rt.version == "1.0.0"


def test_ruby_runtime():
    """Ruby Runtime Tests"""
    ruby_rt = Ruby("1.0.0")

    assert isinstance(ruby_rt, Ruby) == True
    assert ruby_rt.script != ""
    assert "#!/bin/bash" in ruby_rt.script
    assert isinstance(ruby_rt.versions, dict) == True
    assert len(ruby_rt.versions) > 0
    assert ruby_rt.image != ""
    assert ruby_rt.extension != ""
    assert ruby_rt.version == "1.0.0"


def test_rust_runtime():
    """Rust Runtime Tests"""
    rust_rt = Rust("1.0.0")

    assert isinstance(rust_rt, Rust) == True
    assert rust_rt.script != ""
    assert "#!/bin/bash" in rust_rt.script
    assert isinstance(rust_rt.versions, dict) == True
    assert len(rust_rt.versions) > 0
    assert rust_rt.image != ""
    assert rust_rt.extension != ""
    assert rust_rt.version == "1.0.0"
