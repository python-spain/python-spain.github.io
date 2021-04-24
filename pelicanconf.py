#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Python España'
SITENAME = 'Python España'
SITEURL = ''
SITESUBTITLE = 'Web de la Asociación'
SITEIMAGE = '/images/logo.png'
HIDE_AUTHORS = True

PATH = 'content'

TIMEZONE = 'Europe/Madrid'

DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# Icons are provided by https://fontawesome.com/icons (free version)
ICONS = (
    ('fab fa-twitter', 'https://twitter.com/python_es'),
    ('fab fa-github', 'https://github.com/python-spain'),
    ('fab fa-youtube', 'https://www.youtube.com/c/PythonEspa%C3%B1aOficial'),
    ('fas fa-globe-americas', 'http://planet.es.python.org'),
    ('fab fa-telegram', 'https://t.me/PythonEsp'),
    ('fab fa-discourse', 'https://comunidad.es.python.org/'),
    ('fab fa-discord', 'https://discord.gg/35E3Ph7Fez'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = 'themes/pelican-alchemy/alchemy'

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}


def open_absolute_urls_in_blank(attrs, new=False):
    """Detect abosulte URLs (i.e. those starting with the http(s) protocol
    and force them to be open in a new window/tab."""

    _href = attrs.get((None, 'href'), 'nada')
    if _href.startswith('http://') or _href.startswith('https://'):
        attrs[(None, 'target')] = '_blank'

    return attrs

# Configure MARKDOWN extension according to:
# https://github.com/getpelican/pelican/wiki/Tips-n-Tricks

MARKDOWN = {
    'extensions': ['mdx_linkify'],
    'extension_configs': {
        'markdown.extensions.extra': {},
        'markdown.extensions.headerid': {},
        'linkify': {'linkify_callbacks': [open_absolute_urls_in_blank]}
    },
    'output_format': 'html5'
}