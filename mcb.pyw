#! python3
# mcb.pyw - クリップボードのテキストを保存-復元
#Usage:
#py.exe mcb.pyw save <keyword>
#py.exe mcb.pyw <keyword>
#py.exe mcb.pyw list

import shelve, pyperclip, sys

mcb_shelf = shelve.open('mcb')

# TODO: クリップボードの内容を保存

# TODO: キワード一覧と、内容の読み込み

mcb_shelf.close()
