import re

def strip_func(word,*chara):
    if chara:
        l_strip_regex = re.compile(r'^%s*' % chara[0])
        r_strip_regex = re.compile(r'%s*$' % chara[0])
    else:
        l_strip_regex = re.compile('(^\s*)', re.VERBOSE)
        r_strip_regex = re.compile('(\s*$)', re.VERBOSE)

    word = l_strip_regex.sub('',word)
    word = r_strip_regex.sub('',word)
    return word

word1 = '   b  aaaa bbb  cccc   111  '
word2 = 'XXXXb  aaaa XX bbb  cccc   111XXXXX'

print(strip_func(word1))
print(strip_func(word2,'X'))
