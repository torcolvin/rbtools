#
#!/usr/bin/env python
# setup.py -- Installation for rbtools.
#
# Copyright (C) 2009 Christian Hammond
# Copyright (C) 2009 David Trowbridge
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages
from setuptools.command.test import test

from rbtools import get_package_version, is_release, VERSION


PACKAGE_NAME = 'RBTools'

if is_release():
    download_url = "http://downloads.reviewboard.org/releases/%s/%s.%s/" % \
                   (PACKAGE_NAME, VERSION[0], VERSION[1])
else:
    download_url = "http://downloads.reviewboard.org/nightlies/"


install_requires = []


try:
    import json
except ImportError:
    install_requires.append('simplejson')


rb_commands = [
    'close = rbtools.commands.rbclose:Close',
    'diff = rbtools.commands.rbdiff:Diff',
    'patch = rbtools.commands.rbpatch:Patch',
    'post = rbtools.commands.rbpost:Post',
]

setup(name=PACKAGE_NAME,
      version=get_package_version(),
      license="MIT",
      description="Command line tools for use with Review Board",
      entry_points={
          'console_scripts': [
              'post-review = rbtools.postreview:main',
              'rb = rbtools.commands.rb:main',
          ],
          'rb_commands': rb_commands,
      },
      install_requires=install_requires,
      dependency_links=[
          download_url,
      ],
      packages=find_packages(),
      include_package_data=True,
      maintainer="Christian Hammond",
      maintainer_email="chipx86@chipx86.com",
      url="http://www.reviewboard.org/",
      download_url=download_url,
      classifiers=[
          "Development Status :: 4 - Beta",
          "Environment :: Console",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Software Development",
      ]
)
