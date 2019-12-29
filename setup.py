from setuptools import setup
from codecs import open
import io
import os
import os.path
import os
import sys
import sysconfig

pjoin = os.path.join
here = os.path.abspath(os.path.dirname(__file__))
PREFIX = sysconfig.get_config_vars()['prefix']
name = 'aat.crypto'


def get_version(file, name='__version__'):
    path = os.path.realpath(file)
    version_ns = {}
    with io.open(path, encoding="utf8") as f:
        exec(f.read(), {}, version_ns)
    return version_ns[name]

version = get_version(pjoin(here, 'aat', 'crypto', '_version.py'))

with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

if sys.version_info.major < 3 or sys.version_info.minor < 7:
    raise Exception('Must be python3.7 or above')


requires = [
    'aat>=0.0.3',
]

requires_dev = [
    'flake8>=3.7.8',
    'mock',
    'pybind11',
    'pytest>=4.3.0',
    'pytest-cov>=2.6.1',
    'Sphinx>=1.8.4',
    'sphinx-markdown-builder>=0.5.2',
] + requires


setup(
    name=name,
    version=version,
    description='Algorithmic trading library',
    long_description=long_description,
    url='https://github.com/timkpaine/aat.crypto',
    author='Tim Paine',
    author_email='timothy.k.paine@gmail.com',
    license='Apache 2.0',
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

    keywords='algorithmic trading cryptocurrencies',
    packages=['aat.crypto'],
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    extras_require={'dev': requires_dev},
)
