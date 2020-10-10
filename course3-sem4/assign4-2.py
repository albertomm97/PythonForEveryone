# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
pos = int(input('Pos - ')) - 1
repeat = int(input('Repeat - '))

# Retrieve all of the anchor tags
links = list()
names = list()
i = 0
while i < repeat: 
    print("Retrieving: ", url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    tag  = tags[pos]
    links.append(tag.get('href', None))
    names.append(tag.contents[0])
    url = links[i]
    i = i + 1

print(names[len(names) - 1])
    
    

    



