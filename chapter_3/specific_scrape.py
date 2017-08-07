from urllib.request import urlopen

import re
from bs4 import BeautifulSoup

pages = set()
def getlinks(url):
    html = urlopen("http://en.wikipedia.org"+url)
    bs4Obj = BeautifulSoup(html.read(), "html.parser")

    try:
        # title of the page under: h1s
        print("Title: " + bs4Obj.h1.get_text())

        # All paragraph text lives under the div#mw-content-text -> p tag
        paragraph_text = bs4Obj.find(id="mw-content-text").findAll("p")[0].get_text()
        # We are interested in first one, so take first one - [0] from the list
        print("Text: " + paragraph_text)

        # All the paragraph text
        # for l in paragraph_text:
        #    print(l)

        # All the Contents links under div#toc -> ul
        # links_text = bs4Obj.find(id="toc").findAll("span", {"class": "toctext"})
        # print(links_text)

        # A page can have "Edit" which can be found beside Read, View Source, View History in the top
        links = bs4Obj.find(id="ca-edit").find("span").find("a").attrs['href']
        print("Found Edit: " + links)

    except AttributeError:
        print("This page is missing something !")

    href_pattern = "^(/wiki/)"
    for link in bs4Obj.findAll("a", {"href": re.compile(href_pattern)}):
        if "href" in link.attrs:
            if link.attrs["href"] not in pages:
                pages.add(link.attrs["href"])
                newPage = link.attrs["href"]
                print("-------------------------------\n" + newPage)
                getlinks(newPage) # make recursive call

url = ""
getlinks(url)