#题目003：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，
#请问该数是多少？
#【思路分析】所谓完全平方数是指一个数能表示成某个整数的平方的形式，则是完全平方数。
'''
很多人在解这题时用了解方程的方法，其实没有必要。可以直接用平方根来做。
'''
import math
'''这里引用了数学模块，就可以方便的调用平方根了'''
for i in range(-100,20000):
    x = math.sqrt(i+100)
    y = math.sqrt(i+100+168)
    if x%1==0 and y%1==0:
        print(i)