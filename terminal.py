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