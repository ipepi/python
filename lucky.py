#! python3
# lucky.py - Google検索結果を幾つか開く

import requests, sys, webbrowser ,bs4

print('GooGling...')
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)
link_elems = soup.select('.r a')

num_open = min(5, len(link_elems))
for i in range(num_open):
    webbrowser.open('http://google.com' + link_elems[i].get('href'))
