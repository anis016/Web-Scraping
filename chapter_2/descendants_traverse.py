from urllib.error import HTTPError, URLError

from bs4 import BeautifulSoup
from urllib.request import urlopen

def getBS4Object(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print("HTTP Error. Page not retrievable from the serve")
    except URLError as e:
        print("URL Error. URL is not correct or Server is down.")
    else:
        bs4_object = BeautifulSoup(html.read(), "html.parser")
        return bs4_object

url = "http://www.pythonscraping.com/pages/page3.html"
bs4Obj = getBS4Object(url)

# scrape the table contents with id=giftList

# find only descendants that are children. Use the .children tag:
# children: exact one tag below a parent.
# descendants: any level in a tree below the parent. (default)
for child in bs4Obj.find("table", {"id": "giftList"}).children:
    print(child)

# note, there is a possibility to use .descendants tag also.
# if used .descendants tag, then all the tags will be found within the table will be printed
# Simple example: You're the child of your mother,
#                 but YOUR children wouldn't be considered her children
#                 they would, however, be her descendants.