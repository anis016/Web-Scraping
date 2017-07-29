from urllib.error import HTTPError, URLError
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Scrape the page: http://www.pythonscraping.com/pages/warandpeace.html according to CSS class

def getBS4Object(url):
    # Add the Error Handlers
    try:
        html = urlopen(url)
    except HTTPError as e:
        print("HTTP Error. Page not retrievable from the serve")
    except URLError as e:
        print("URL Error. URL is not correct or Server is down.")
    else:
        bs4_obj = BeautifulSoup(html.read(), "html.parser")
        return bs4_obj

url = "http://www.pythonscraping.com/pages/warandpeace.html"
bs4Obj = getBS4Object(url)

# print(bs4Obj.h1) # check if url is correct and retrievable

# scrape all the class tag "green" :
# <span class="green">the prince</span>

# bsObj.findAll(tagName, tagAttributes)
nameList = bs4Obj.findAll("span", {"class": "green"}) # Returns empty list if nothing found
# print(nameList)
if not (nameList == []):
    for name in nameList:
        print(name.get_text())
else:
    print("class does not exist.")