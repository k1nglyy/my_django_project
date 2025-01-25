import os
import sys
sys.path.insert(0, os.path.abspath('../../../'))

# -- Project information -----------------------------------------------------

project = 'My_Django_Project'
copyright = '2025, Daniil Polyanskiy'
author = 'Daniil Polyanskiy'
release = '1.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary',
]

autosummary_generate = True

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'
html_static_path = ['_static']
html_sidebars = {
    "**": [
        "globaltoc.html",
        "relations.html",  # needs 'show_powered_by': False in conf.py to hide "Powered by"
        "searchbox.html",
    ]
}
html_theme_options = {
    "show_powered_by": False,
}