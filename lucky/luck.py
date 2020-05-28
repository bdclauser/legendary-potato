#! python3
# luck.py - Opens several Google search results.

import requests
import sys
import webbrowser
import bs4

print('Googling...')  # diplay text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1]))
res.raise_for_status()

# Retrive top search result links.
soup = bs4.BeautifulSoup(res.text)

# Open a browser tab for each result.
linksElems = soup.select('.r a')
numOpen = min(5, len(linksElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linksElems[i].get('href'))
