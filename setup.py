#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
    name='exploitdb',
    version='0.1.0',
    description="Shell-style script to search exploit-db.com exploits.",
    long_description=readme,
    author="Mathieu D.",
    author_email='email@example.com',
    url='https://github.com/mattoufoutu/exploitdb',
    py_modules=['exploitdb'],
    include_package_data=True,
    license="MIT license",
    zip_safe=False,
    keywords='exploitdb',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    entry_points={'console_scripts': [
        'exploitdb = exploitdb:main'
    ]}
)
