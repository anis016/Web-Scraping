from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page1.html")

# default parse is "html.parser"
bsObj = BeautifulSoup(html.read(), "html.parser")

# below all the 3 produces same output
print(bsObj.h1)
print(bsObj.body.h1)
print(bsObj.html.body.h1) # actually: html -> body -> h1