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

import uuid
import json
from .lang import Lang


class Code():
    """Code To Run"""

    def __init__(self, code, lang, version, id=None, meta = {}):
        self._code = code
        self._lang = lang
        self._version = version
        self._id = str(uuid.uuid4()) if id is None else id
        self._meta = meta

    @property
    def code(self):
        """
        Gets the code snippet

        Returns:
            The code snippet
        """
        return self._code

    @property
    def lang(self):
        """
        Gets the language type

        Returns:
            The language type
        """
        return self._lang

    @property
    def version(self):
        """
        Gets the language version

        Returns:
            The language version
        """
        return self._version

    @property
    def id(self):
        """
        Gets the code instance ID

        Returns:
            The code instance ID
        """
        return self._id

    @property
    def meta(self):
        """
        Gets the code meta data

        Returns:
            The code meta data
        """
        return self._meta

    @classmethod
    def from_string(cls, data):
        """
        Get Code from JSON string

        Args:
            data: the JSON string

        Returns:
            An instance of this class
        """
        data = json.loads(data)

        return cls(
            data['code'],
            Lang.get_item(data['lang']),
            data['version'],
            data['id'],
            data['meta']
        )

    def __str__(self):
        """
        Convert the Object to string

        Returns:
            A JSON representation of this instance
        """
        return json.dumps({
            'id': self._id,
            'code': self._code,
            'lang': self._lang.value,
            'version': self._version,
            'meta': self._meta,
        })
