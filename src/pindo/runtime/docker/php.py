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


class PHP():
    """PHP Runtime Class"""

    # Docker Image
    _image = "php"

    # Default Version
    _version = "7.4"

    # All supported versions
    # curl 'https://registry.hub.docker.com/v2/repositories/library/php/tags/?page_size=1000&page=1&name=..' -s | jq '."results"[]["name"]
    _versions = {
        "7.0": "Version 7.0",
        "7.1": "Version 7.1",
        "7.2": "Version 7.2",
        "7.3": "Version 7.3",
        "7.4": "Version 7.4",
        "8.0": "Version 8.0",
        "8.1": "Version 8.1",
    }

    # File extension
    _extension = "php"

    def __init__(self, version="7.4"):
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
            "php /tmp/run.php",
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
