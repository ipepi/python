#! python3
# mcb.pyw - クリップボードのテキストを保存-復元
#Usage:
#py.exe mcb.pyw save <keyword> - クリップボードをキーボードを紐付けて保存
#py.exe mcb.pyw <keyword> - キーワードに紐付けられたテキストをクリップボードにコピー
#py.exe mcb.pyw list - 全キーワードをクリップボードにコピー
#py.exe mcb.pyw delete <keyword > - shelfからをキーボードを削除

import shelve, pyperclip, sys

mcb_shelf = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()

elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    if sys.argv[2] in mcb_shelf.keys():
        del mcb_shelf[sys.argv[2]]

elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])

mcb_shelf.close()
