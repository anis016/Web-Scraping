from urllib.request import urlopen

import re
from bs4 import BeautifulSoup

html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bs4Obj = BeautifulSoup(html.read(), "html.parser")

# Finding all the links
# for link in bs4Obj.findAll("a"):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])

# Grab first: <div id="bodyContent" class="mw-body-content">
# pattern: /wiki/Kyle_Chandler       [Check only these. This link leads to Article]
# pattern: /wiki/Special:Random      [Ignore these]
# re.compile("^(/wiki/)((?!:).)*$")) [ ((?!:).)* --> ignores /wiki/ with ':' in there]
link_pattern = "^(/wiki/)((?!:).)*$"
for link in bs4Obj.find("div", {"id": "bodyContent"}).findAll("a",
                                                              {"href": re.compile(link_pattern)}):
    if "href" in link.attrs:
        print(link.attrs["href"])