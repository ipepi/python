birthdays = {"アリス":'4/1', 'ボブ':'12/12', 'キャロル':'4/4'}

while True:
    print('名前を入力して下さい：(終了するにはEnterだけをおしてください)')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(name + 'の誕生日は' + birthdays[name])
    else:
        print(name + 'の名前は未登録です。')
        print('誕生日を入力して下さい：')
        bday = input()
        birthdays[name] = bday
        print('誕生日データベースを更新しました')
