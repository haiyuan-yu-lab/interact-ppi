# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
import sphinx_rtd_theme


#sys.path.insert(0, os.path.abspath(os.path.join("..", "..", "module")))

sys.path.insert(0, os.path.abspath('../module'))

# Print debugging information
print("Current working directory:", os.getcwd())
print("Module path:", os.path.abspath('../module'))
print("sys.path:", sys.path)



project = 'INTERACT-PPI'
copyright = '2024, Yu lab'
author = 'Yu lab'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


extensions = ["sphinx.ext.autodoc", "sphinx.ext.viewcode", "sphinx.ext.napoleon"]

templates_path = ['_templates']
exclude_patterns = []




html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'collapse_navigation': False,
    'display_version': True,
    'navigation_depth': 3,
}
html_static_path = ['_static']
html_css_files = ['css/custom.css']


'''
# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
# alabaster or sphinx_rtd_theme
html_theme = 'sphinx_rtd_theme' 
#html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ['_static']
'''

autosummary_generate = True
