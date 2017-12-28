'''数あてゲーム'''
import random
SECRET_NUMBER = random.randint(1, 20)
print('1から20までの数を当てて下さい。')
GUESS = int(input())

#6回聞く
for guess_taken in range(1, 7):
    print('数を入力してください')
    GUESS = int(input())
    if GUESS < SECRET_NUMBER:
        print('小さいです')
    elif GUESS > SECRET_NUMBER:
        print('大きいです')
    else:
        break

if GUESS == SECRET_NUMBER:
    print('あたり!' + str(guess_taken) + '回であたりました')
else:
    print('残念。正解は ' + str(SECRET_NUMBER) + 'でした')
