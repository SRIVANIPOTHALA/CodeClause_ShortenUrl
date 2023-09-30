import pyshorteners
url = input("Enter The URL :")


def shorturl(url) :
    s = pyshorteners.Shortener()
    print(s.tinyurl.short(url))


shorturl(url)