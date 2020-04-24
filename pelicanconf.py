#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

LOAD_CONTENT_CACHE = False

AUTHOR = u'Evan Downing'
SITENAME = u'Evan Downing'
SITEURL = ''

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

PATH = 'content'
PAGE_PATHS = ['page']
ARTICLE_PATHS = ['blog']
STATIC_PATHS = ['page','blog','image','file']

EXTRA_PATH_METADATA = {
    'file/CNAME': {'path': 'CNAME'},
    'image/favicon.ico': {'path': 'favicon.ico'},
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

ICONS = [
    ('rss', 'feeds/all.rss.xml'),
]

GOOGLE_ANALYTICS = 'UA-139439777-1'

MENUITEMS = (
    ('About', '/pages/about.html'),
    ('CV', '/file/Downing_CV.pdf'),
    ('Projects', '/pages/projects.html'),
    ('PGP', '/file/pgp_public.asc'),
    ('Github', 'https://github.com/evandowning'),
    ('Google Scholar', 'https://scholar.google.com/citations?user=SnJNwIAAAAAJ&hl=en'),
)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

USE_FOLDER_AS_CATEGORY = True

###############
# Theme stuff #
###############

THEME = 'theme/pelican-blueidea'

# Display pages list on the top menu
DISPLAY_PAGES_ON_MENU = False

# Display categories list on the top menu
DISPLAY_CATEGORIES_ON_MENU = False

# Display categories list as a submenu of the top menu
DISPLAY_CATEGORIES_ON_SUBMENU = True

# Display the category in the article's info
DISPLAY_CATEGORIES_ON_POSTINFO = True

# Display the author in the article's info
DISPLAY_AUTHOR_ON_POSTINFO = False

# Display the search form
DISPLAY_SEARCH_FORM = False

# Sort pages list by a given attribute
#PAGES_SORT_ATTRIBUTE (Title)

# Display the "Fork me on Github" banner
#GITHUB_URL (None)

# Blogroll
#LINKS 

# Social widget
#SOCIAL
