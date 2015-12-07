# -*- coding: utf-8 -*-
#
# crypto-enigma documentation build configuration file, created by
# sphinx-quickstart on Sat Nov 28 14:45:20 2015.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
import shlex

sys.path.insert(0, os.path.abspath('../..'))
from crypto_enigma._version import __version__, __release__, __author__

# See - http://stackoverflow.com/q/1733414/656912; http://stackoverflow.com/a/34030206/656912
# Use in doctest_global_setup instead
# reload(sys)
# sys.setdefaultencoding("UTF-8")

# Has no effect -- http://stackoverflow.com/q/34025113/656912
sys.dont_write_bytecode = True

# TBD - Has no effect, but something like this is needed <<<
#       http://stackoverflow.com/q/33977457/656912
#       https://github.com/sphinx-doc/sphinx/issues/1711
# from functools import wraps, update_wrapper
# def no_op_wraps(func):
#     """Replaces functools.wraps in order to undo wrapping.
#
#     Can be used to preserve the decorated function's signature
#     in the documentation generated by Sphinx.
#
#     """
#     def wrapper(decorator):
#         return func
#     return wrapper
#
# wraps = no_op_wraps
# update_wrapper = lambda wrapper, func: func

# Add a directive to get just the docstring
# See - http://stackoverflow.com/a/7832437/656912
from sphinx.ext import autodoc

class SimpleDocumenter(autodoc.MethodDocumenter):
    objtype = "simple"

    #do not indent the content
    content_indent = ""

    #do not add a header to the docstring
    def add_directive_header(self, sig):
        pass

def setup(app):
    app.add_autodocumenter(SimpleDocumenter)

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.3'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.extlinks'
    #'sphinx_paramlinks' # Not working witn Googly docstrings - http://stackoverflow.com/a/20845306/656912
    # 'alabaster',
    # 'sphinxarg.ext',
    # 'sphinxcontrib.programoutput',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'crypto-enigma'
copyright = u'2014-2015, ' + __author__
author = __author__

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = __release__
# The full version, including alpha/beta/rc tags.
release = __version__
# Note: The above is correct; the terms are the reverse of those used in PEP404

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all
# documents. - http://sphinx-doc.org/domains.html#python-roles
default_role = 'py:obj'

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = False

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
modindex_common_prefix = ['crypto_enigma.']

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


rst_epilog = """
.. |se| replace:: StackExchange
.. _`StackExchange`: http://stackexchange.com
.. _`SE`: http://stackexchange.com
.. |repo_link| replace:: <https://github.com/orome/crypto-enigma-py/>
.. _machine models: http://www.cryptomuseum.com/crypto/enigma/tree.htm
.. _development version: https://github.com/orome/crypto-enigma-py/tree/develop
.. _test versions: https://testpypi.python.org/pypi/crypto-enigma
.. _milestones: https://github.com/orome/crypto-enigma-py/milestones
.. _open issues: https://github.com/orome/crypto-enigma-py/issues
.. _new issues: https://github.com/orome/crypto-enigma-py/issues/new
.. _Enigma machines: http://en.wikipedia.org/wiki/Enigma_machine
.. _simple substitution encoding: https://en.wikipedia.org/wiki/Substitution_cipher
.. _Ringstellung: https://en.wikipedia.org/wiki/Enigma_rotor_details#Ring_setting
.. |mappings| replace:: :ref:`mappings <mapping_encoding>`
.. |mapping| replace:: :ref:`mapping <mapping_encoding>`
.. |Walzenlage| replace:: *Walzenlage*
.. _Walzenlage: http://www.cryptomuseum.com/crypto/enigma/working.htm
.. |Walzenstellung| replace:: *Walzenstellung*
.. _Walzenstellung: http://www.cryptomuseum.com/crypto/enigma/working.htm
.. |Steckerverbindungen| replace:: *Steckerverbindungen*
.. _Steckerverbindungen: http://www.cryptomuseum.com/crypto/enigma/working.htm
.. |Ringstellung| replace:: *Ringstellung*
.. _Haskell version: https://hackage.haskell.org/package/crypto-enigma
.. _Hackage documentation: https://hackage.haskell.org/package/crypto-enigma/docs/Crypto-Enigma.html
"""



# Extension settings

# sphinx.ext.napoleon - https://sphinxcontrib-napoleon.readthedocs.org/en/latest/#configuration
# napoleon_google_docstring = True
napoleon_numpy_docstring = False
# napoleon_include_private_with_doc = False
# napoleon_include_special_with_doc = True
# napoleon_use_admonition_for_examples = False
# napoleon_use_admonition_for_notes = False
# napoleon_use_admonition_for_references = False
# napoleon_use_ivar = False
# napoleon_use_param = True
# napoleon_use_rtype = True

# sphinx.ext.autodoc - http://sphinx-doc.org/ext/autodoc.html
autodoc_member_order = 'bysource'
# Incorporate __init__ documentation into the class documentation;
# See: - http://sphinx-doc.org/ext/autodoc.html#confval-autoclass_content
autoclass_content = 'class'

# sphinx.ext.extlinks - http://sphinx-doc.org/ext/extlinks.html
extlinks = {
    'github': ('https://github.com/%s', ''),
    'git-tag': ('https://github.com/orome/crypto-enigma-py/releases/tag/%s', ''),
    'git-commit': ('https://github.com/orome/crypto-enigma-py/tree/%s', ''),
    'physics.se': ('http://physics.stackexchange.com/%s', ''),
    'so': ('http://stackoverflow.com/%s', '')
}

# sphinx.ext.doctest - http://sphinx-doc.org/ext/doctest.html
doctest_test_doctest_blocks = 'docs'
doctest_global_setup = (
    '#encoding: utf8\n\n'
    'from __future__ import unicode_literals #Has no effect?\n'
    'import sys\n'
    'reload(sys)\n'
    'sys.setdefaultencoding("UTF-8")\n'
    'from crypto_enigma.machine import *\n'
)


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {
#     #'logo': 'logo.png',
#     'github_user': 'orome',
#     'github_repo': 'crypto-enigma-py',
#     'github_button': True,
#     'github_banner': True,
#     'travis_button': True
# }

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr'
#html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
#html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'crypto-enigmadoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',

# Latex figure (float) alignment
#'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  (master_doc, 'crypto-enigma.tex', u'crypto-enigma Documentation',
   author, 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'crypto-enigma', u'crypto-enigma Documentation',
     [author], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  (master_doc, 'crypto-enigma', u'crypto-enigma Documentation',
   author, 'crypto-enigma', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}
