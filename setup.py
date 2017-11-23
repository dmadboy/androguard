#!/usr/bin/env python
import sys
import os
from androguard import __version__

from setuptools import setup, find_packages

# workaround issue on OSX, where sys.prefix is not an installable location
if sys.platform == 'darwin' and sys.prefix.startswith('/System'):
    data_prefix = os.path.join('.', 'share', 'androguard')
elif sys.platform == 'win32':
    data_prefix = os.path.join(sys.prefix, 'Scripts', 'androguard')
else:
    data_prefix = os.path.join(sys.prefix, 'share', 'androguard')

# There is a bug in pyasn1 0.3.1, 0.3.2 and 0.3.3, so do not use them!
install_requires = ['pyasn1!=0.3.1,!=0.3.2,!=0.3.3,!=0.4.1',
                    'future',
                    'networkx',
                    'pygments',
                    ]

# python version specific library versions:
#
# IPython Issue: For python2.x, a version <6 is required
if sys.version_info >= (3, 3):
    install_requires.append('ipython>=5.0.0')
else:
    install_requires.append('ipython>=5.0.0,<6')

# pycrypography >= 2 is not supported by py3.3
# See https://cryptography.io/en/latest/changelog/#v2-0
if sys.version_info.major == 3 and sys.version_info.minor == 3:
    install_requires.append('cryptography>=1.0,<2.0')
else:
    install_requires.append('cryptography>=1.0')

setup(
    name='androguard',
    description='Androguard is a full python tool to play with Android files.',
    version=__version__,
    packages=find_packages(),
    data_files=[(data_prefix,
                 ['androguard/gui/annotation.ui',
                  'androguard/gui/search.ui',
                  'androguard/gui/androguard.ico'])],
    scripts=['androaxml.py',
             'androlyze.py',
             'androdd.py',
             'androgui.py',],
    install_requires=install_requires,
    extras_require={
        'GUI': ["pyperclip", "PyQt5"],
        # We support the following three magic packages:
        # * filemagic from https://pypi.python.org/pypi/filemagic
        # * file-magic from https://pypi.python.org/pypi/file-magic  (which is the "offical" one, and also in Debian)
        # * python-magic from https://pypi.python.org/pypi/python-magic
        # If you are installing on debian you can use python3-magic instead, which fulfills the dependency to file-magic
        'magic': ['file-magic'],
        'docs': ['sphinx', 'sphinxcontrib-programoutput', 'sphinx_rtd_theme'],
        'graphing': ['pydot'],
    },
    setup_requires=['setuptools'],

)
