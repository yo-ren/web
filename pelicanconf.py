#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
 
AUTHOR = u'Yo-ren Limited'
SITENAME = u'Yo-ren Co.,Ltd'
ARCHIVES = u'Archives'

SITEURL = ''

PATH = 'content'
HIDE_SITENAME = True

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_TAGS_ON_SIDEBAR = True
SOCIAL = False


THEME = 'theme'
SITELOGO = 'theme/images/yoren_logo_white.png'
BOOTSTRAP_THEME = 'sandstone'


BANNER = 'theme/images/banner.jpeg'
BANNER_SUBTITLE = 'Digital Marketing'

#Article Specific Options
SHOW_ARTICLE_AUTHOR = True
SHOW_ARTICLE_CATEGORY = True
DISPLAY_BREADCRUMBS = True


# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
          # ('Another social link', '#'),)

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ['../pelican-plugins/']
PLUGINS = ['i18n_subsites',]

I18N_SUBSITES = {
    'ja': {
        'SITENAME': '有限会社・遊仁堂',
        'ARCHIVES': 'アーカイブ'
    },
    'zh': {
        'SITENAME': '有限公司・游仁堂',
        'ARCHIVES': '归档'
    },
}

# Language Settings
languages_lookup = {
    'ja': '日本語',
    'zh': '简体中文',                                                
    'en': 'English',                                                
}

def lookup_lang_name(lang_code):
    return languages_lookup[lang_code]

JINJA_FILTERS = {
    'lookup_lang_name': lookup_lang_name,
}
