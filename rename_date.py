#! python3
# rename_date.py - 米国式日付MM-DD-YYYYのファイル名を欧州式DD-MM-YYYYに書き換える

import shutil, os, re
#米国式日付MM-DD-YYYYのファイル名にマッチングする正規表現を作る

date_pattern = re.compile(r"""^(.*?)
    ((0|1)?\d)-
    ((0|1|2|3)?\d)-
    ((19|20)\d\d)
    (.*?)$
    """, re.VERBOSE)

# TODO: カレントディレクトリの全ファイルをループする

# TODO: 日付のないファイルをスキップする

# TODO: ファイル名を部分分解する

# TODO: 欧州式の日付ファイル名を作る

# TODO: ファイルのフルパス(絶対パス)を取得する

# TODO: ファイル名を変更する



