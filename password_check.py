import re
import sys

#8文字以上のチェック
def check1(word):
    check_regex1 = re.compile(r'''
    ([a-zA-Z0-9]){8,}
    ''',re.VERBOSE)
    mo1 = check_regex1.search(word)
    return mo1 != None

#小文字の英字が含まれている
def check2(word):
    check_regex2 = re.compile(r'''(
    [a-z]
    )''',re.VERBOSE)
    mo2 = check_regex2.search(word)
    return mo2 != None

#大文字の英字が含まれている
def check3(word):
    check_regex3 = re.compile(r'''(
    [A-Z]
    )''',re.VERBOSE)
    mo3 = check_regex3.search(word)
    return mo3 != None

#数字が含まれている
def check4(word):
    check_regex4 = re.compile(r'''(
    [0-9]
    )''',re.VERBOSE)
    mo4 = check_regex4.search(word)
    return mo4 != None

if len(sys.argv) < 2:
    print('使い方:python password_check.py [パスワード]')

password = sys.argv[1]

if(check1(password) and check2(password) and check3(password) and check4(password)):
    print('パスワードとして十分です')
else:
    print('パスワードが弱いです')

