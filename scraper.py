# this is a webcrawler
import urllib2

pageOpener = urllib2.build_opener()
pageOpener.addheaders = [{'User-agent', 'Mozilla/5.0'}]

url = ('https://nodejs.org/en/')

openURL = pageOpener.open(url).read()

print(openURL)
