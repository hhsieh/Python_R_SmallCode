import pandas as pd
import urllib
import urlparse
import re
from bs4 import BeautifulSoup

# all links have the same structure

Links = ["http://www.newyorksocialdiary.com/party-pictures?page=" + str(i) for i in range(3,27)]
Rs = [urllib.urlopen(Link).read() for Link in Links]
soups = [BeautifulSoup(R, "lxml") for R in Rs]
As = [soup.find_all('a', href=True) for soup in soups]

#parties = [[a["href"] for a in soup.select('a[href*=party-pictures]')] for soup in soups]
#print(parties)

## This one is even better! :)
pattern = re.compile(r"/party-pictures/")
parties = [[a["href"] for a in soup.find_all('a', href=pattern)] for soup in soups]
flattened_parties = []
for party in parties:
    for y in party:
        flattened_parties.append(y)

#print(len(flattened_parties)) #1193

## Make new soups with all of the 1193 links
NewLinks = ["http://www.newyorksocialdiary.com" + flattened_parties[i] for i in range(len(flattened_parties))]
NewRs = [urllib.urlopen(NewLink).read() for NewLink in NewLinks]

import pickle
file_Name = "soupsfile"
fileObject = open(file_Name, 'wb')
pickle.dump(NewRs, fileObject)
fileObject.close()

## open the file for reading
fileObject = open(file_Name, 'r')
#load the object from the file into var b
NewRs = pickle.load(fileObject)

NewSoups = [BeautifulSoup(NewR) for NewR in NewRs]
