from datetime import datetime

AUTHOR = "Evan Downing"
SITEURL = "http://localhost:8000"
SITENAME = "Evan Downing"
SITETITLE = "Evan Downing"
SITESUBTITLE = "Cybersecurity Researcher"
SITEDESCRIPTION = "Evan's personal website."
SITELOGO = SITEURL + "/images/profile.png"
FAVICON = SITEURL + "/images/favicon.ico"
BROWSER_COLOR = "#333333"
PYGMENTS_STYLE = "monokai"

ROBOTS = "index, follow"

THEME = "../pelican-themes/Flex"
PATH = "content"
OUTPUT_PATH = "blog/"
TIMEZONE = "America/New_York"

DISABLE_URL_HASH = True

PLUGIN_PATHS = ["../pelican-plugins"]

PLUGINS = ["post_stats", "deadlinks"]

I18N_TEMPLATES_LANG = "en"
DEFAULT_LANG = "en"
OG_LOCALE = "en_US"
LOCALE = "en_US"

DATE_FORMATS = {
    "en": "%B %d, %Y",
}

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = True
MAIN_MENU = True
HOME_HIDE_TAGS = True
LINKS_IN_NEW_TAB = False

LINKS = (
    ("Resume", "https://docs.google.com/document/d/1sKsh88ZiiveotGS-KR4l-vESgfj_U_JifvH6nGat-Wk"),
    ("CV", "https://docs.google.com/document/d/1UcXkHeRCKpBvlf4KyW92GKjyEeoiPgXGdW7ARPSa2L4"),
)

SOCIAL = (
    ("github", "https://github.com/evandowning"),
    ("google", "https://scholar.google.com/citations?user=SnJNwIAAAAAJ&hl=en"),
    ("linkedin", "https://www.linkedin.com/in/evandowning/"),
    ("mixcloud", "https://www.mixcloud.com/evandowning/"),
)

MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)

CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike 4.0 International License",
    "version": "4.0",
    "slug": "by-sa",
    "icon": True,
    "language": "en_US",
}

COPYRIGHT_YEAR = datetime.now().year
DEFAULT_PAGINATION = 5

STATIC_PATHS = ["images", "extra/CNAME", "extra/custom.css"]

EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
    "extra/custom.css": {"path": "static/custom.css"},
}

CUSTOM_CSS = "static/custom.css"

THEME_COLOR = "light"
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = False
THEME_COLOR_ENABLE_USER_OVERRIDE = True

USE_LESS = True

ALWAYS_MODIFIED = True

DEADLINK_OPTS = {
    'archive':  True,
    'classes': ['custom-class1', 'disabled'],
    'labels':   True,
    'timeout_duration_ms': 1000,
    'timeout_is_error':    False,
}

