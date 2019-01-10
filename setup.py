from setuptools import setup, find_packages
from codecs import open
from os import path
import platform

here = path.abspath(path.dirname(__file__))

# get requirements
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    requirements = f.read().splitlines()

# description for pypi
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    desc = f.read()

setup(
    name='blammisc',
    version='0.0.1',
    description='Miscellaneous tools for BLAM experiments.',
    long_description=desc,
    long_description_content_type='text/markdown',
    url='https://github.com/aforren1/blammisc',
    author='Alexander Forrence',
    author_email='aforren1@jhu.edu',
    license='GPL3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GPL3 License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    install_requires=requirements,
    keywords='blam',
    packages=find_packages(exclude=['contrib', 'docs', 'tests'])
)