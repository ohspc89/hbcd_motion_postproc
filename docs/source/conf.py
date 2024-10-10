# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'hbcd-motion-postproc'
copyright = '2024, Infant Neuromotor Control Laboratory'
author = 'Jinseok Oh'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinxarg.ext'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
        'navigation_depth': 4,
        'style_external_links': True,
        }

html_context = {
        "display_github": True,
        "github_user": "Infant-Neuromotor-Control-Lab",
        "github_repo": "hbcd_motion_postproc",
        "github_version": "main",
        "conf_py_patch": "/docs/",

        # Docker link added as an external resource
        "docker_url": "https://hub.docker.com/repository/docker/inclab/hbcd_motion_postproc/general",
        }

html_static_path = ['_static']
html_css_files = ['custom.css']

# -- Options for EPUB output
epub_show_urls = 'footnote'
