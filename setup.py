"""Setuptools for cloudsteak.
	CloudSteak - Cloud Tools by The1bit
"""
# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

import sys


here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'docs/readme.rst'), encoding='utf-8') as f:
	long_description = f.read()

# Get the license description from the license file
with open(path.join(here, 'docs/LICENSE.txt'), encoding='utf-8') as l:
	license_description = l.read()


## Version of the current package
from bin.version import __version__

sys.stdout.write("cloudsteak: " + __version__ + '\n')


# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(name='cloudsteak',
	scripts=['cloudsteak'],
	install_requires=['azure-cli','awscli','docopt'],
	python_requires='>=2.6, <3',
    version=__version__,
	description='CloudSteak - Cloud Tools by the1bit',
	long_description=long_description + "\n" + license_description,
	url='https://github.com/the1bit/cloudsteak',
	author='Tibor Kiss',
	author_email='the1bithu@gmail.com',
	keywords='cloud azure aws management python microsoft the1bithu',
	classifiers=[  # Optional
		# How mature is this project? Common values are
		#   3 - Alpha
		#   4 - Beta
		#   5 - Production/Stable
		'Development Status :: 3 - Alpha',

		# Indicate who your project is intended for
		'Intended Audience :: Developers',
		'Topic :: Software Development :: Build Tools',
		'Operating System :: POSIX :: Linux',

		# Pick your license as you wish
		'License :: OSI Approved :: MIT License',

		# Specify the Python versions you support here. In particular, ensure
		# that you indicate whether you support Python 2, Python 3 or both.
		'Programming Language :: Python',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 2.7'
	],
	  packages=['bin'],
	  license='MIT',
	  zip_safe=True)