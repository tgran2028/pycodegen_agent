#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Tim Gran",
    author_email='timothyrgran@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Code generation for python",
    entry_points={
        'console_scripts': [
            'pycodegen_agent=pycodegen_agent.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pycodegen_agent',
    name='pycodegen_agent',
    packages=find_packages(include=['pycodegen_agent', 'pycodegen_agent.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/tgran2028/pycodegen_agent',
    version='0.1.0',
    zip_safe=False,
)
