def collatz(number):
    if number % 2 == 0:
        return int(number / 2)
    elif number % 2 == 1:
        return int(3 * number + 1)


try:
    print('整数を入力してください：')
    INPUT_NUMBER = int(input())
    ANSER = INPUT_NUMBER#ansernにINPUT_NUMBERを代入
    while True:
        ANSER = collatz(ANSER)
        print(ANSER)
        if ANSER == 1:
            break
except ValueError:
    print('入力値が整数ではありません。整数を入力して下さい:')
