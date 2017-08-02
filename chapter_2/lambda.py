from urllib.error import HTTPError, URLError
from urllib.request import urlopen
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

# finding all the tags that have exactly two attributes
# ex: tr tag has two attributes: class and id
# <tr class="gift" id="gift1">
# 	<td>
# 		Vegetable Basket
# 	</td>
# 	<td>
# 		This vegetable basket is the perfect gift for your health conscious (or overweight) friends!
# 		<span class="excitingNote">Now with super-colorful bell peppers!</span>
# 	</td>
# 	<td>
# 		$15.00
# 	</td>
# 	<td>
# 		<img src="../img/gifts/img1.jpg"/>
# 	</td>
# </tr>
tags = bs4Obj.findAll(lambda tag: len(tag.attrs) == 2)
print(tags)