# -*- coding: utf-8 -*-
from setuptools import setup


setup(
    name='uu_sphinx_theme',
    py_modules=['uu_sphinx_theme'],
    packages=['uu_sphinx_theme'],
    include_package_data=True,
    package_data={'uu_sphinx_theme': [
        'theme.conf',
        '*.html',
        'static/*.*',
    ]},
    version='1.0.0',
    entry_points={
        "sphinx.html_themes": [
            "uu_sphinx_theme = uu_sphinx_theme"
        ]
    },
    install_requires=[
        'sphinx'
    ]
)
