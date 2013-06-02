from lice import __version__
from setuptools import setup, find_packages
import sys

long_description = open('README.rst').read()

extra_kwargs = {}
if sys.version_info < (2, 7):
    extra_kwargs['setup_requires'] = ['argparse>=1.2', 'unittest2']
if sys.version_info >= (3,):
    extra_kwargs['setup_requires'] = ['setuptools']

setup(
    name="lice",
    version=__version__,
    author="Jeremy Carbaugh",
    author_email="jcarbaugh@gmail.com",
    url='https://github.com/licenses/lice',
    description='Generate a license file for a project',
    long_description=long_description,
    license='BSD',
    packages=find_packages(),
    package_data={'lice': ['*.txt']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['lice = lice:main']},
    platforms=['any'],
    test_suite='lice.tests.collector',
    classifiers=[
        'Development Status :: 5 - Production',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    **extra_kwargs
)
