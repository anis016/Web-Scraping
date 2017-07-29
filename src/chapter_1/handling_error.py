from urllib.error import HTTPError, URLError
from urllib.request import urlopen
from bs4 import BeautifulSoup

try:
    html = urlopen("http://www.pythonscraping.com/pages/page1.html")

# The page is not found on the server (or there was some error in retrieving it).
except HTTPError as e:
    print(e)

# If the server is not found at all (if, say, http://www.pythonscraping.com was down, or the URL was mistyped)
except URLError as e:
    print("The Server Could not be found!")
else:
    # program continues as it is
    bs4Obj = BeautifulSoup(html.read(), "html.parser")
    try:
        # content = bs4Obj.nonExistentTag # This will return None Object.
        # content = bs4Obj.nonExistentTag.noTag # This will throw AttributeError
        content = bs4Obj.h1

        # If encountered any tag that is accessing a tag on None Object, it will throw AttributeError.
    except AttributeError as e:
        print("Tag was not found. AttributeError")
    else:
        # Trying to access a tag that is not present is going to return None Object.
        if content is None:
            print("Tag was not found")
        else:
            print(bs4Obj.h1)