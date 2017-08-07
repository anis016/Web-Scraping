import datetime
import random
from urllib.request import urlopen
from urllib.request import urlparse
from bs4 import BeautifulSoup
import re

pages = set() # checks for duplicate
random.seed(datetime.datetime.now()) # for generating initial random seed value

def getInternalLinks(bs4Obj, url):
    includeUrl = urlparse(url).scheme+"://"+urlparse(url).netloc
    internalLinks = []

    href_pattern = "^(/\.*" + includeUrl + ")"
    for link in bs4Obj.findAll("a", {"href": href_pattern}):
        attrs_href = link.attrs["href"]
        if attrs_href is not None:
            if attrs_href not in internalLinks:
                if attrs_href.startswith("/"):
                    internalLinks.append(includeUrl + attrs_href)
                else:
                    internalLinks.append(attrs_href)

    return internalLinks