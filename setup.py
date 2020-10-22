# -*- coding: utf-8 -*-
import os
import re
from setuptools import setup, find_namespace_packages

# Get README and remove badges.
README = open('README.rst').read()
README = re.sub('----.*marker', '----', README, flags=re.DOTALL)

DESCRIPTION = ('Samsung remote control using the Multiple Display Control '
               'Protocol via TCP/IP')

NAME = 'samsung_remote_control'

setup(
    name=NAME,
    python_requires='>3.5.0',
    description=DESCRIPTION,
    long_description=README,
    author='Pieter Smets',
    author_email='mail@pietersmets.be',
    url='https://github.com/psmsmets/samsung_remote_control',
    download_url='https://github.com/psmsmets/samsung_remote_control.git',
    license='GNU General Public License v3 (GPLv3)',
    packages=find_namespace_packages(include=[f'{NAME}.*']),
    keywords=['samsung', 'display', 'remote', 'control', 'automation',
              'mdc', 'tcp/ip'],
    entry_points={
        'console_scripts': [
           f'{NAME}={NAME}.__main__:main',
        ],
    },
    scripts=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        ('License :: OSI Approved :: ' +
         'GNU General Public License v3 (GPLv3)'),
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        "Topic :: Home Automation",
        "Topic :: Multimedia :: Video :: Display"
    ],
    install_requires=[
        'pysimplegui >= 4.0.0',
        'samsung_mdc',
    ],
    use_scm_version={
        'root': '.',
        'relative_to': __file__,
        'write_to': os.path.join(NAME, 'version.py'),
    },
    setup_requires=['setuptools_scm'],
)
