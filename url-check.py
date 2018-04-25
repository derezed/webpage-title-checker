import csv
import urllib2
from bs4 import BeautifulSoup

contents = []

with open('urls.csv','r') as csvf:
    urls = [row for row in csv.reader(csvf.read().splitlines())]
    for url in urls:
        contents.append(url)

for url in contents:
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Google Chrome')]
    print url
    response = opener.open(url[0])
    page = response.read()

    soup = BeautifulSoup(page, 'lxml')

    titles = soup.find_all('title')

    if len(titles) > 1:
        print "%s has too many title tags." % url
    elif len(titles) <= 0:
        print "%s has potentially no title tags." % url
