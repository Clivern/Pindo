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

from pindo.lang import Lang


def test_lang():
    """Lang Tests"""

    assert Lang.RUBY.value == "ruby"
    assert Lang.RUST.value == "rust"
    assert Lang.JAVA.value == "java"
    assert Lang.GO.value == "go"
    assert Lang.PYTHON.value == "python"
    assert Lang.PHP.value == "php"

    assert Lang.get_item("ruby") == Lang.RUBY
    assert Lang.get_item("rust") == Lang.RUST
    assert Lang.get_item("java") == Lang.JAVA
    assert Lang.get_item("go") == Lang.GO
    assert Lang.get_item("python") == Lang.PYTHON
    assert Lang.get_item("php") == Lang.PHP
