#题目005：输入三个整数x,y,z，请把这三个数由小到大输出。
#【思路分析】虽然可以考虑用if-then语句，不过如果比较的数据增加，显然就不合适了。
'''
这里用列表的sorted()函数显然更加方便
'''
print('请按要求输入数字：')
l=[]
for a in range(3):
    x=int(input('请输入一个整数：'))
    l.append(x)

print(sorted(l))
