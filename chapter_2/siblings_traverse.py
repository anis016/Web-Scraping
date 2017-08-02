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

# find the next siblings. Use the .next_siblings callback of a tag.
for sibling in bs4Obj.find("table", {"id": "giftList"}).tr.next_siblings:
    print(sibling)

# print(bs4Obj.find("img", {"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())
# 1.The image tag where src = "../img/gifts/img1.jpg" is first selected
# 2.We select the parent of that tag( in this case, the < td > tag).
# 3.We select the previous_sibling of the < td > tag( in this case, the < td > tag that contains
#   the dollar value of the product).
# 4.We select the text within that tag, "$15.00"

# note, similar like .children tag except the first first row is skipped.
# because, Objects cannot be siblings with themselves.
# Any time you get siblings of an object, the object itself will not be included in the list.

# siblings: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#next-sibling-and-previous-sibling