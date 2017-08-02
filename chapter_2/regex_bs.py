from urllib.error import HTTPError, URLError
from urllib.request import urlopen

import re
from bs4 import BeautifulSoup

# Scrape the page: http://www.pythonscraping.com/pages/warandpeace.html according to CSS class

def getBS4Object(url):
    # Add the Error Handlers
    try:
        html = urlopen(url)
    except HTTPError as e:
        print("HTTP Error. Page not retrievable from the server")
    except URLError as e:
        print("URL Error. URL is not correct or Server is down.")
    else:
        bs4_obj = BeautifulSoup(html.read(), "html.parser")
        return bs4_obj

url = "http://www.pythonscraping.com/pages/page3.html"
bs4Obj = getBS4Object(url)

# ../img/gifts/img1.jpg
# \.\.\/img\/gifts\/img1\.jpg
image = "\.\.\/img\/gifts\/img[\d]+\.jpg"
pattern = re.compile(image)
images = bs4Obj.findAll("img", {"src": pattern})
# print(images)
for img in images:
    print(img['src'])