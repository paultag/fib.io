# -*- coding: utf-8 -*-
from __future__ import unicode_literals

AUTHOR = 'Paul Tagliamonte'
SITENAME = "Paul's Hacks"
SITEURL = 'http://fib.io'
TIMEZONE = "America/New_York"
THEME = "fib"

GITHUB_URL = 'http://github.com/paultag/'
# DISQUS_SITENAME = "blog-notmyidea"
PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
# LOCALE = ['en_US.utf8', 'en_US']

DEFAULT_PAGINATION = 4
DEFAULT_DATE = (2013, 3, 2, 14, 1, 1)

FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

LINKS = (('Blog', 'http://blog.pault.ag'),)

SOCIAL = (('twitter', 'http://twitter.com/paultag'),
          ('lastfm', 'http://lastfm.com/user/paultag'),
          ('identica', 'http://identi.ca/paultag'),
          ('github', 'http://github.com/paultag'),)

# global metadata to all the contents
DEFAULT_METADATA = ()  #(('yeah', 'it is'),)

# static paths will be copied under the same name
STATIC_PATHS = []  #"pictures", ]

# A list of files to copy from the source to the destination
FILES_TO_COPY = ()  # (('extra/robots.txt', 'robots.txt'),)

# custom page generated with a jinja2 template
TEMPLATE_PAGES = {}  # 'pages/jinja2_template.html': 'jinja2_template.html'}
