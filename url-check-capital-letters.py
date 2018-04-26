import csv
import urllib2
from bs4 import BeautifulSoup

contents = []

with open('capital-letters.csv','r') as csvf:
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

    links = soup.find_all('a')

    for link in links:
        href = link.get('href')
        for x in href:
            if x.isupper():
                print "%s has capital letters" % href
