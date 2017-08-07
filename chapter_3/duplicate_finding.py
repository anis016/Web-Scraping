from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# Use Set DS to avoid duplicates

pages = set()
def getlinks(pageURL):
    global pages # accessing global variable inside a function
    html = urlopen("http://en.wikipedia.org"+pageURL)
    bs4Obj = BeautifulSoup(html.read(), "html.parser")

    # pattern: /wiki/
    wiki_pattern = "^(/wiki/)"
    for link in bs4Obj.findAll("a", {"href": re.compile(wiki_pattern)}):
        if "href" in link.attrs:
            if link.attrs["href"] not in pages:
                # we have encountered a new Page
                new_page = link.attrs["href"]
                print(new_page)
                pages.add(new_page)
                getlinks(new_page)

wiki_url = ""
getlinks(wiki_url)