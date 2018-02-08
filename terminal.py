import os
my_files = ['accounts.txt', 'detail.csv', 'invite.docx']
for filenames in my_files:
    print(os.path.join('usr/bin/spam',filenames))


import shelve
shelf_file = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Shimon']
shelf_file['cats'] = cats
shelf_file.close



shelf_file = shelve.open('mydata')
type(shelf_file)
shelf_file['cats']
shelf_file.close


import pprint
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
pprint.pformat(cats)

file_obj = open('myCats.py', 'w')
file_obj.write('cats = ' + pprint.pformat(cats) + '\n')
file_obj.close

import myCats
myCats.cats

import os
for foldername, subfolders, filenames in os.walk('/Users/Ippei/python'):
    print('The current folder is ' + foldername)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + foldername + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + foldername + ': ' + filename)
        print(' ')


import zipfile, os
os.chdir('/Users/Ippei/python/folder')
example_zip = zipfile.ZipFile('example.zip')

import zipfile, os
os.chdir('/Users/Ippei/python/folder')
example_zip = zipfile.ZipFile('example.zip')
example_zip.namelist()

spam_info = example_zip.getinfo('spam.txt')
spam_info.file_size

example_zip.extractall()

import zipfile
new_zip = zipfile.ZipFile('new.zip', 'w')
new_zip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
new_zip.close()

import requests, bs4
res = requests.get('http://nostarch.com')
res.raise_for_status()
no_starch_soup = bs4.BeautifulSoup(res.text)
type(no_starch_soup)

import requests, bs4
example_file = open('example.html')
example_soup = bs4.BeautifulSoup(example_file)
type(example_soup)

elems = example_soup.select('#author')
type(elems)
len(elems)
type(elems[0])
elems[0].getText()
str(elems[0])
elems[0].attrs

