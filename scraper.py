# this is a webcrawler made with python 3.85
import urllib.request
import urllib.parse
import re

#variable to keep program keep_running
keep_running = True
url = ''


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

#function to display page stats
def display_stats(linkn):
    print("\n")
    print("*" * 20)
    print("I Have found " + str(linkn) + " links hardcoded and\n")
    print("I found " + str(linkn) + " internal links from\n" + url)

#find the links in data
def find_links(my_data):
    link_count = 0
    my_data = my_data.read()
    my_data = str(my_data, encoding = 'utf-8') #needed to split data otherwise it is bytecode
    #using regular expression to find all href in http document.
    links = re.findall(r'href="(.*?)">',my_data)

    '''
    the following code makes sure link and url are concatenated correctly
    '''
    
    for link in links:
        if(link.startswith('http')):
            print(link)
            link_count = link_count + 1
        if(not link.startswith('http')):
            if(url.endswith('/') and not link.startswith('/')):
                link = url + link
                link_count = link_count + 1
                print(link)
            elif(not url.endswith('/') and link.startswith('/')):
                link = url + link
                link_count = link_count + 1
                print(link)
            elif(not url.endswith('/') and not link.startswith('/')):
                link = url + '/' + link
                link_count = link_count + 1
                print(link)
            elif(url.endswith('/') and link.startswith('/')):
                link = url + link.strip('/')
                link_count = link_count + 1
                print(link)
            else:
                print("something went wrong you didn't account for idiot")
        
    return link_count
'''
    depricated function

    split_data = my_data.split()
    for word in split_data:
        if(word.startswith('href')):
            print(word)
'''
introduction()

while keep_running:
    url = ask_user()
    url_page = get_page(url)
    num_of_links = find_links(url_page)
    display_stats(num_of_links)
    user_answer = input("Would you like to visit another page(y/n): ")
    if user_answer.lower() == "n":
        keep_running = False
