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


class Elixir():
    """Elixir Runtime Class"""

    # Docker Image
    _image = "elixir"

    # Default Version
    _version = "1.14.2"

    # All supported versions
    _versions = {
        "1.7.4": "Version 1.7.4",
        "1.8.2": "Version 1.8.2",
        "1.9.4": "Version 1.9.4",
        "1.10.4": "Version 1.10.4",
        "1.11.4": "Version 1.11.4",
        "1.12.3": "Version 1.12.3",
        "1.13.4": "Version 1.13.4",
        "1.14.2": "Version 1.14.2",
    }

    # File extension
    _extension = "exs"

    def __init__(self, version="3.0"):
        """Class Constructor"""
        self._version = version

    @property
    def script(self):
        """
        Get execution script content

        Returns:
            the execution script content
        """
        return "\n".join([
            "#!/bin/bash",
            "",
            "mkdir -p /tmp",
            "cp -r /code/* /tmp/",
            "cd /tmp",
            "start_time=$(date +%s%N)",
            "elixir /tmp/run.exs",
            "elapsed=$((($(date +%s%N) - $start_time)/1000000))",
            "echo \"-------\"",
            "echo \"Execution time in milliseconds: \"$elapsed",
            "",
        ])

    @property
    def versions(self):
        """
        Get all supported versions

        Returns:
            A dict of supported versions
        """
        return self._versions

    @property
    def image(self):
        """
        Get docker image name

        Returns:
            the docker image
        """
        return self._image

    @property
    def version(self):
        """
        Get the default version

        Returns:
            the default version
        """
        return self._version

    @property
    def extension(self):
        """
        Get the extension

        Returns:
            the extension
        """
        return self._extension
