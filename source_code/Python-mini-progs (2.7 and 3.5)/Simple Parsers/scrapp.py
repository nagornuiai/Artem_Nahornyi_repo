### FOR PYTHON 2.7 ###

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
limit = int(raw_input("Enter amount of iterations\n>>>"))
pos = int(raw_input("Enter the position of required element\n>>>")) - 1
count = 0
while count < limit:
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
    tags = soup('a')
    print tags[pos].get('href', None)
    url = tags[pos].get('href', None)
    count = count + 1