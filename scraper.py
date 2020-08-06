# this is a webcrawler
import urllib2

pageOpener = urllib2.build_opener()
pageOpener.addheaders = [{'User-agent', 'Mozilla/5.0'}]

url = raw_input("Enter a web page: ")

openURL = pageOpener.open(url).read()

print(openURL)
for word in openURL.split(' '):
    if word.startswith('href'):
        print(word)
