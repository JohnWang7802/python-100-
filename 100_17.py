#输入一行字符，分别统计出其中英文字母、空格、数字和其他字符的个数
#【思路分析】对于字符有判断其类型的方法，isalpha,isspace,isdigit

s=input("请从键盘任意输入字符：")
letter,space,digit,others=0,0,0,0
for c in s:
    if c.isalpha():
        letter +=1
    elif c.isspace():
        space +=1
    elif c.isdigit():
        digit +=1
    else:
        others +=1
print('英文字母有 %d 个，空格数有 %d 个，数字有 %d 个，其他字符有 %d 个'%(letter,space,digit,others))

