"""This is exitExample.py"""
import sys

while True:
    print('終了するにはexitと入力してください。')
    RESPONSE = input()
    if RESPONSE == 'exit':
        sys.exit()
    print(RESPONSE + 'と入力されました。')
