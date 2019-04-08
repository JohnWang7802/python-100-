#题目019：找出1000以内的完数
#【思路分析】所谓完数，就是指一个数除自身以外，所有的约数之和，等于它本身的数为完数。
'''
继续用数列求和的方法，把一个数的约束全部记下来
'''

for number in range(1,1000):
    arr=[]
    for i in range(1,number):
        if number % i ==0:
            arr.append(i)
    if sum(arr)==number:
        print(number,arr)
