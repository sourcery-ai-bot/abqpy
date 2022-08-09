# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

import inspect
import os
import re
import sys
import typing

project = 'abqpy'
copyright = '2022, WANG Hailin'
author = 'WANG Hailin'

# The full version, including alpha/beta/rc tags
release = '2016a10'

# -- General configuration ---------------------------------------------------

# Add source code
sys.path.insert(0, os.path.abspath('../../src'))

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_toolbox.more_autodoc.overloads',
    'autoclasstoc',
    'sphinx.ext.autodoc',
    'sphinx_autodoc_typehints',
    'numpydoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.linkcode',
    'sphinx.ext.githubpages',
    'sphinx_copybutton',
]


# linkcode source
def linkcode_resolve(domain: str, info: dict[str, typing.Union[str, list[str]]]):
    """Resolve linkcode source
    Parameters
    ----------
    domain : str
        specifies the language domain the object is in
    info : dict[str, str | list[str]]
        a dictionary with the following keys guaranteed to be present (dependent on the domain)

        - py: module (name of the module), fullname (name of the object)
        - c: names (list of names for the object)
        - cpp: names (list of names for the object)
        - javascript: object (name of the object), fullname (name of the item)

    Returns
    -------
    source url of the object
    """
    if domain != 'py':
        return None

    modname = info['module']
    fullname = info['fullname']

    filename = modname.replace('.', '/')
    main_release = release.split(".")[0][:4]
    baseurl = f'https://github.com/haiiliin/abqpy/blob/V{main_release}/src/{filename}.py'

    submod = sys.modules.get(modname)
    if submod is None:
        return baseurl

    obj = submod
    for part in fullname.split('.'):
        try:
            obj = getattr(obj, part)
        except Exception:
            return baseurl
    try:
        source, lineno = inspect.getsourcelines(obj)
    except TypeError:
        # Find source line for an attribute, the obj is None
        attr = fullname.split('.')[-1]
        obj = submod
        for part in fullname.split('.')[:-1]:
            try:
                obj = getattr(obj, part)
            except Exception:
                return baseurl
        source, lineno = inspect.getsourcelines(obj)
        attr_sources: list[str] = re.findall(rf'\n(    {attr}: [\w\W]+?)\n\n', '\n'.join(source))
        if len(attr_sources) > 0:
            attr_source = attr_sources[0].splitlines()

            def find_line_number(string: str, text: list[str]):
                for line_number, line in enumerate(text):
                    if string in line:
                        return line_number

            index = find_line_number(attr_source[0], source)
            for row in range(index - 1, -1, -1):
                if source[row].startswith('    #: '):
                    attr_source.insert(0, source[row])
                else:
                    break
            lineno += find_line_number(attr_source[0], source)
            source = attr_source
    except Exception:
        return baseurl

    return baseurl + f'#L{lineno}-L{lineno + len(source) - 1}'


# Show short type hints for user-defined classes and defaults for parameters
python_use_unqualified_type_names = True
autodoc_typehints_format = 'short'
typehints_defaults = 'comma'
typehints_document_rtype = False

autodoc_default_options = {
    'undoc-members': False,
}

numpydoc_show_class_members = False
numpydoc_show_inherited_class_members = False
numpydoc_xref_param_type = True
add_module_names = False

# Figure numbering
numfig = True

# True to convert the type definitions in the docstrings as references. Defaults to False.
napoleon_preprocess_types = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'furo'

# Logo
# html_logo = "_static/3ds-dark.svg"


html_theme_options = {
    'navigation_depth': 9,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Options for LaTeX output -------------------------------------------------

# If true, add page references after internal references. This is very useful
# for printed copies of the manual. Default is False.
latex_show_pagerefs = True

# Control whether to display URL addresses. This is very useful for printed
# copies of the manual. The setting can have the following values:
# 'no' - do not display URLs (default)
# 'footnote' - display URLs in footnotes
# 'inline' - display URLs inline in parentheses
latex_show_urls = 'footnote'

# If given, this must be the name of an image file (relative to the
# configuration directory) that is the logo of the docs. It is placed at the
# top of the title page. Default: None.
latex_logo = None

# The “theme” that the LaTeX output should use. It is a collection of settings
# for LaTeX output (ex. document class, top level sectioning unit and so on).
# As a built-in LaTeX themes, manual and howto are bundled.
# manual
# A LaTeX theme for writing a manual. It imports the report document class
# (Japanese documents use jsbook).
# howto
# A LaTeX theme for writing an article. It imports the article document class
# (Japanese documents use jreport rather). latex_appendices is available only for this theme.
# It defaults to 'manual'.
latex_theme = 'manual'

# autoclass_content = 'both'

latex_toplevel_sectioning = 'part'
latex_engine = 'xelatex'
latex_use_xindy = False
latex_elements = {
    'preamble': '\\usepackage[UTF8]{ctex}\n\\setcounter{tocdepth}{3}\n\\setcounter{secnumdepth}{5}',
    'printindex': '\\def\\twocolumn[#1]{#1}\\printindex',
}
