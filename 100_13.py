#题目013：打印“水仙花数”
#【编程思路】水仙花数是指一个三位数，各个数字的立方和等于它本身
'''
只要了解通过//（整除下取整）和%（除法取余）两个运算符即可把三位数的个十百位的数字取出即可。
'''
for i in range(100,1000):
    h=i//100
    t=i%100//10
    n=i%10
    if h**3+t**3+n**3==i:
        print(i)
        
