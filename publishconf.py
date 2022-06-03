import os
import sys

sys.path.append(os.curdir)

try:
    from pelicanconf import *
except ImportError:
    sys.path.append(os.path.join(os.curdir, "docs"))
    from pelicanconf import *

SITEURL = "https://www.evandowning.com"

RELATIVE_URLS = False

USE_LESS = False

GOOGLE_ANALYTICS = 'UA-139439777-1'
