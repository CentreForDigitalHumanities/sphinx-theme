# -*- coding: utf-8 -*-
from setuptools import setup


setup(
    name='uu-sphinx-theme',
    version='1.0.0',
    entry_points={
        "sphinx.html_themes": {
            "uu_sphinx_theme": "uu_sphinx_theme"
        }
    }
)
