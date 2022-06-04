import os
import sys

sys.path.append(os.curdir)

try:
    from pelicanconf import *
except ImportError:
    sys.path.append(os.path.join(os.curdir, "docs"))
    from pelicanconf import *

SITEURL = "https://www.evandowning.com"
SITELOGO = SITEURL + "/images/profile.png"
FAVICON = SITEURL + "/images/favicon.ico"

RELATIVE_URLS = False

USE_LESS = False

GOOGLE_ANALYTICS = 'G-C0W4PHDF8Y'
