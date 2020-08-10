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


class Ruby():
	"""Ruby Runtime Class"""

	# Docker Image
	_image = "ruby"

	# Default Version
	_version = "3.0"

	# All supported versions
	_versions = {
		"2.6": "Version 2.6",
		"2.6.1": "Version 2.6.1",
		"2.6.2": "Version 2.6.2",
		"2.6.3": "Version 2.6.3",
		"2.6.4": "Version 2.6.4",
		"2.6.5": "Version 2.6.5",
		"2.6.6": "Version 2.6.6",
		"2.6.7": "Version 2.6.7",
		"2.6.8": "Version 2.6.8",
		"2.6.9": "Version 2.6.9",
		"2.7.0": "Version 2.7.0",
		"2.7.1": "Version 2.7.1",
		"2.7.3": "Version 2.7.3",
		"2.7.4": "Version 2.7.4",
		"2.7.5": "Version 2.7.5",
		"3.0.0": "Version 3.0.0",
	}

	# File extension
	_extension = "rb"

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
			"start_time=$(date +%s.%3N)",
			"ruby /code/run.rb",
			"end_time=$(date +%s.%3N)",
			"elapsed=$(echo \"scale=3; $end_time - $start_time\" | bc)",
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

