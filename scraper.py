# this is a webcrawler
import urllib.request
import urllib.parse





myHeader =  {'User-Agent':'Mozilla/5.0'}
#ask user for web page if none given use default and if http forgotten it is appended
def ask_user():
    url = input("Enter a url for me to visit: ")
    if url == "":
        url = "http://phobos.ninja"
    elif not url.startswith("http"):
        url = "https://" + url
        print("I added https:// for you, you lazy bastard!\n")
    return url


#basic get web page
def get_page(page):

    pageData = urllib.request.urlopen(page)
    readData = pageData.read()
    print(readData)

url = ask_user()
get_page(url)
