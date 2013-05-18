from lice.core import __version__
from setuptools import setup, find_packages

long_description = open('README.rst').read()

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
)
