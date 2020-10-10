import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
print(html)
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all the anchor tags
links = soup("a")
for link in links:
    print(link.get("href", None))