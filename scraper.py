# this is a webcrawler
import urllib.request
import urllib.parse
import re


myHeader =  {'User-Agent':'Mozilla/5.0'}
#ask user for web page if none given use default and if http forgotten it is appended
def ask_user():
    url = input("Enter a url for me to visit: ")
    if url == "":
        url = "http://phobos.ninja"
        print("Fetching default page http://phobos.ninja because it is teh awesomeness!\n")
    elif not url.startswith("http"):
        url = "https://" + url
        print("I added https:// for you, you lazy bastard!\n")
    return url


#basic get web page
def get_page(page):
    try:
        pageData = urllib.request.urlopen(page)
        return pageData
    except(e):
        print(str(e))

#find the links in data
def find_links(my_data):
    my_data = my_data.read()
    my_data = str(my_data, encoding = 'utf-8') #needed to split data otherwise it is bytecode
    split_data = my_data.split()
    for word in split_data:
        if(word.startswith('href')):
            print(word)


url = ask_user()
url_page = get_page(url)
find_links(url_page)
