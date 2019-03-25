#题目012：判断101——200之间有多少个素数，并把这些素数输出
#【编程思路】素数就是因数除了1和其本身的数，考虑到一个数的因数最大就到它的平方根，因此一个循环就可以搞定了
'''
for循环中可以用break跳出循环
'''
import math

total=0

for i in range(101,201):
    flag=0
    k=int(math.sqrt(i+1))
    for j in range(2,k+1):
        if i % j==0:
            flag=1
            break
    if flag==0:
        print(i)
        total+=1
print('101--200之间共有%d个素数' %(total))
