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


def test_code():
    """Code Tests"""
    code = Code("puts 'Hello World'", Lang.RUBY, "3.0.0")

    assert isinstance(code, Code) == True
    assert code.code == "puts 'Hello World'"
    assert code.version == "3.0.0"
    assert code.lang == Lang.RUBY
    assert code.lang.value == "ruby"
    assert code.id != ""

    new_code = Code.from_string(str(code))

    assert isinstance(new_code, Code) == True
    assert new_code.code == code.code
    assert new_code.version == code.version
    assert new_code.lang == code.lang
    assert new_code.lang.value == code.lang.value
    assert new_code.id == code.id
