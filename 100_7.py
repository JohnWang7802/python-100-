#题目007：将一个列表的数据复制到另一个列表中
#【思路分析】列表的操作，复制是个重点，直接的b=a,其实还是一个列表，只是在a的地址前又插了面旗而已
'''
列表的复制一定要用切片的方法
'''
a = [1,2,3,4]
b = a[:]
