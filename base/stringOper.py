# coding=utf-8

#计算字符串中字母,数字,空格数量
s = raw_input('input a string: \n')
letters = 0
space = 0
digit = 0
others = 0
for c in s:
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1
print 'char=%d,space=%d,digit=%d,others=%d' % (letters,space,digit,others)