"""pp107 4.10.1 add_comma.py"""
def add_comma(sample_list):
    sample_list[len(sample_list) - 1] = 'and ' + sample_list[len(sample_list) - 1]
    moji = ''
    for i in range(len(sample_list)):
        moji += sample_list[i]
        if i != len(sample_list)-1:
            moji += ', '
    return moji

spam = ['apple', 'bananas', 'tofu', 'cats']
print(add_comma(spam))
