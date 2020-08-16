# this is a webcrawler made with python 3.85
import urllib.request
import urllib.parse
import re

#variable to keep program keep_running
keep_running = True

def introduction():
    print("*"*24)
    print("* Welcome to Crawlfish *")
    print("* The Best Web Crawler *")
    print("*"*24)
    print("\n")

myHeader =  {'User-Agent':'Mozilla/5.0'}
#ask user for web page if none given use default and if http forgotten it is appended
def ask_user():


    url = input("Enter a url for me to visit:(enter for default page) ")
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
    #using regular expression to find all href in http document.
    links = re.findall(r'href="(.*?)">',my_data)
    for link in links:
        print(link)
        #next I need to add page url to relative links


'''
    split_data = my_data.split()
    for word in split_data:
        if(word.startswith('href')):
            print(word)
'''
introduction()

while keep_running:
    url = ask_user()
    url_page = get_page(url)
    find_links(url_page)
    user_answer = input("Would you like to visit another page(y/n): ")
    if user_answer.lower() == "n":
        keep_running = False
