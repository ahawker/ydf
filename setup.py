"""
    ydf
    ~~~

    YAML to Dockerfile.

    :copyright: (c) 2017 Andrew Hawker.
    :license: Apache 2.0, see LICENSE file.
"""

import ast
import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


version_regex = re.compile(r'__version__\s+=\s+(.*)')


def get_version():
    with open('ydf/__init__.py', 'r') as f:
        return str(ast.literal_eval(version_regex.search(f.read()).group(1)))


setup(
    name='ydf',
    version=get_version(),
    author='Andrew Hawker',
    author_email='andrew.r.hawker@gmail.com',
    url='https://github.com/ahawker/ydf',
    license='Apache 2.0',
    description='YAML to Dockerfile',
    long_description=__doc__,
    packages=['ydf'],
    install_requires=[
        'click',
        'jinja2',
        'ruamel.yaml',
        'six'
    ],
    entry_points="""
        [console_scripts]
        ydf=ydf.cli:main
    """,
    classifiers=(
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules'
    )
)
