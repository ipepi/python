#! python3
# coding:utf-8
# mapIt.py - コマンドラインやクリップボードに指定した住所の地図を開く

import webbrowser, sys
import pyperclip
if len(sys.argv) > 1:
    #コマンドラインから住所ぞ取得する
    address = ' '.join(sys.argv[1:])
else:
    # クリップボードから住所を取得する
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

