#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

DELETE_OUTPUT_DIRECTORY = True

AUTHOR = 'Mark Kirby'
SITENAME = 'markkirby.me'
SITESUBTITLE = 'Technology Doer'
SITEURL = 'http://localhost:8000'

# This is used to copy static files to the output directory
STATIC_PATHS = ['images', 'pdfs']
PAGE_PATHS = ['pages']
PATH = 'content'
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'

TIMEZONE = 'America/New_York'

THEME = "./theme_two"

#PAGINATED_DIRECT_TEMPLATES = ('categories', 'archives')

PLUGIN_PATHS = ['H:/plugins/pelican-plugins','plugins']
PLUGINS = ['representative_image','neighbors']

DEFAULT_LANG = 'English'
IGNORE_FILES = ['__pycache__']
TYPOGRIFY = True

#set this a FALSE FOR NOW - DEVELOPMENT
LOAD_CONTENT_CACHE = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


DEFAULT_PAGINATION = 10

PLUGINS = ['encrypt_content']
ENCRYPT_CONTENT = {
    'title_prefix': '[Encrypted]',
    'summary': 'This content is encrypted.'
}




# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#themes i like
# flex https://github.com/alexandrevicenzi/Flex/tree/5bc235cf579cb03bcc8f54b6029ff74493a0cb44
# pelican-blue https://github.com/Parbhat/pelican-blue/tree/1dda054242f9267f4bd49891b022ac41c9ecfbe8
# pelican-striped-html5up https://github.com/getpelican/pelican-themes/tree/master/pelican-striped-html5up
# bootstrap2 https://github.com/getpelican/pelican-themes/tree/master/bootstrap2
# crowsfoot https://github.com/porterjamesj/crowsfoot/tree/30509fc0cf6d4c29f2d1d9ec87783340a7158538
# Lannisport  https://github.com/siovene/lannisport/tree/a36fafd36369602e05c41fa9277967c479ac3c45
# lovers https://github.com/chdoig/pelican-bootstrap3-lovers/tree/234de548b4dd5f5779597fd27075723e80b7384f
