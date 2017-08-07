import datetime
from urllib.request import urlopen

import re
from bs4 import BeautifulSoup
import random

def getlinks(articleurl):
    url = "http://en.wikipedia.org" + articleurl
    html = urlopen(url)
    bs4Obj = BeautifulSoup(html.read(), "html.parser")

    # pattern: /wiki/Kyle_Chandler                           [Check only these. This link leads to Article]
    # pattern: /wiki/Special:Random                          [Ignore these]
    # pattern: //wikimediafoundation.org/wiki/Privacy_policy [Ignore these]
    href_pattern = "^(/wiki/)((?!:).)*$"
    all_links = bs4Obj.find("div", {"id": "bodyContent"}).findAll("a",
                                                              {"href": re.compile(href_pattern)})
    return all_links

random.seed(datetime.datetime.now())
articleurl = '/wiki/Kevin_Bacon'
links = getlinks(articleurl) # get the Kevin Bacon all the article links
while len(links) > 0: # will continue this recursively until no new article present
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"] # get the random "new" Article
    print(newArticle)
    links = getlinks(newArticle) # go inside the random new Article