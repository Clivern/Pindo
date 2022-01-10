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


class Java():
    """Java Runtime Class"""

    # Docker Image
    _image = "openjdk"

    # Default Version
    _version = "11"

    # All supported versions
    # curl 'https://registry.hub.docker.com/v2/repositories/library/openjdk/tags/?page_size=1000&name=16.0' -s | jq '."results"[]["name"]'
    _versions = {
        "10.0": "Version 10.0",
        "11.0": "Version 11.0",
        "12.0": "Version 12.0",
        "13.0": "Version 13.0",
        "14.0": "Version 14.0",
        "15.0": "Version 15.0",
        "16.0": "Version 16.0",
        "17.0": "Version 17.0",
    }

    # File extension
    _extension = "java"

    def __init__(self, version="11", main_class="Run"):
        """Class Constructor"""
        self._version = version
        self._main_class = main_class

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
            "start_time1=$(date +%s%N)",
            "javac {}.java".format(self._main_class),
            "elapsed1=$((($(date +%s%N) - $start_time1)/1000000))",
            "start_time2=$(date +%s%N)",
            "java {}".format(self._main_class),
            "elapsed2=$((($(date +%s%N) - $start_time2)/1000000))",
            "echo \"-------\"",
            "echo \"Build time in milliseconds: \"$elapsed1",
            "echo \"Execution time in milliseconds: \"$elapsed2",
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
    def main_class(self):
        """
        Get the main class name

        Returns:
            the main class name
        """
        return self._main_class

    @property
    def extension(self):
        """
        Get the extension

        Returns:
            the extension
        """
        return self._extension
