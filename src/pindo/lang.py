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

from enum import Enum


class Lang(Enum):
    """Language Types"""

    RUST = "rust"
    GO = "go"
    PHP = "php"
    PYTHON = "python"
    JAVA = "java"
    RUBY = "ruby"
    C = "c"
    CPLUS = "cplus"
    ELIXIR = "elixir"

    @classmethod
    def get_item(cls, key):
        """
        Get Enum key with the value

        Args:
            key: the value

        Returns:
            The key
        """
        if key == "rust":
            return cls.RUST

        elif key == "go":
            return cls.GO

        elif key == "php":
            return cls.PHP

        elif key == "python":
            return cls.PYTHON

        elif key == "java":
            return cls.JAVA

        elif key == "ruby":
            return cls.RUBY

        elif key == "c":
            return cls.C

        elif key == "cplus":
            return cls.CPLUS

        elif key == "elixir":
            return cls.ELIXIR
