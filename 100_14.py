#题目014：将一个正整数分解质因数
#【编程思路】类似手算分解质因数的过程，找出因数后，原数字缩小
'''
找出质因数并不难，把他们打印出来有点小烦
'''

num = int(input('请输入一个整数：'))
original=num

a= []
while num > 1:
    for i in range(2,num+1):
        if num%i == 0:
            a.append(i)
            num = num//i
            break

print("%d ="%(original),end='')
for i in range(len(a)-1):
    print(a[i],end='*')

print(a[len(a)-1])
    
                       
