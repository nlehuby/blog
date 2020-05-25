#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'nlehuby'
SITENAME = 'Le blog de nlehuby'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['initialement_publié_sur_drupalgardens', 'images']

THEME = "blue-penguin-theme"

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

SUMMARY_MAX_LENGTH = 40

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

#Menu blue-penguin
ARCHIVES_URL       = 'archives'
ARCHIVES_SAVE_AS   = 'archives/index.html'

MENU_INTERNAL_PAGES = (
    ('Tous les articles', ARCHIVES_URL, ARCHIVES_SAVE_AS),
)

# additional menu items
MENUITEMS = (
    ('Github', 'https://github.com/nlehuby'),
)

DISPLAY_HEADER = True
DISPLAY_FOOTER = True
DISPLAY_HOME   = True
DISPLAY_MENU   = True
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
