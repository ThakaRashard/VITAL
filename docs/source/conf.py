# Configuration file for the Sphinx documentation builder.
# Documentation: https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

sys.path.insert(0, os.path.abspath('../..'))

# Debugging: Print sys.path to verify
print("sys.path:", sys.path)

# -- Project Information -----------------------------------------------------
project = 'VITAL'
copyright = (
    '2025, National Technology & Engineering Solutions of Sandia, LLC (NTESS). '
    'Under the terms of Contract DE-NA0003525 with NTESS, the U.S. Government retains certain rights in this software.'
)
author = 'Sandia National Laboratories'
release = '0.1'

# -- General Configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',       # Automatically document Python modules
    'sphinx.ext.napoleon',      # Support for Google-style and NumPy-style docstrings
    'sphinx.ext.viewcode',      # Add links to highlighted source code
    'sphinx.ext.mathjax',       # Render mathematical expressions using MathJax
    'sphinx.ext.autosummary',   # Automatically generate summary tables
]

autosummary_generate = True
autosummary_imported_members = True

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- HTML Output Configuration ------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = []
html_show_sourcelink = False


# -- Autodoc Configuration ---------------------------------------------------
autodoc_member_order = 'bysource'
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'private-members': False,
    'special-members': '__init__',
    'show-inheritance': True,
}
autodoc_class_signature = "separated"

# -- Napoleon Configuration --------------------------------------------------
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_use_param = True
napoleon_use_rtype = True
add_module_names = False

# -- Syntax Highlighting -----------------------------------------------------
highlight_language = 'python3'
rst_prolog = """
.. role:: python(code)
   :language: python
"""

# -- MathJax Configuration ---------------------------------------------------
mathjax3_config = {
    'TeX': {
        'equationNumbers': {'autoNumber': 'AMS'},
    }
}

# -- Intersphinx Configuration ------------------------------------------------
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('https://numpy.org/doc/stable', None),
    'pandas': ('https://pandas.pydata.org/docs', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/reference', None),
    'matplotlib': ('https://matplotlib.org/stable', None),
}

# -- Suppress Warnings --------------------------------------------------------
suppress_warnings = ['toc.not_included']