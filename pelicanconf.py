#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ognian Genev'
SITENAME = "Ognian's Blog"
SITEURL = 'https://ogenev.github.io'
SITETITLE = AUTHOR
SITESUBTITLE = 'Data Scientist, Entrepreneur' #needed for theme
SITEDESCRIPTION = 'Ognian Genev Data Science Blog' #used for meta tag for SEO purposes

COPYRIGHT_YEAR = 2019

# Theme Settings
SITELOGO = '/images/me.jpg' #your site logo
# FAVICON = '/images/favicon.png' #your favicon
THEME = '/Users/ogenev/pelican-themes/pelican-themes/Flex'
BROWSER_COLOR = '#333333'
ROBOTS = 'index, follow'
PYGMENTS_STYLE = 'default' #for code highlighting

PATH = 'content'
MAIN_MENU = True

TIMEZONE = 'Europe/Sofia'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('about', '{about.md}/pages'),
  #       ('contact', '#'),
   #      ('portfolio', '#'))

# Social widget
SOCIAL = (('github', 'https://github.com/ogenev'),
          ('linkedin', 'https://www.linkedin.com/in/ognian-genev-989327131/'),)

DEFAULT_PAGINATION = 7
GOOGLE_ANALYTICS = 'UA-131792108-1'

MENUITEMS = (('Archives', '/archives.html'),
            ('Categories', '/categories.html'),
	    ('Tags', '/tags.html'),)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

# if you create jupyter files in the content dir, snapshots are saved with the same
# metadata. These need to be ignored. 
IGNORE_FILES = [".ipynb_checkpoints"]  