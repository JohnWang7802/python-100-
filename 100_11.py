#问题011：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子。假如兔子都不死。问每个月的兔子总数为多少？
#【思路分析】这其实就是斐波拉契数列的由来，可以思考斐波拉契数列的打印过程
'''
实际解决这题时，按照事实的逻辑顺序来解题即可，即：
第一个月有一对小兔子，
第二个月一对小兔子长成了一对大兔子
第三个月，一对大兔子生出了一对小兔子，原本的一对大兔子都不死
每个月的过程是：
大兔子每月生小兔子
原先的小兔子长成2月兔（下月生育）
大兔子不死
'''
smallrabi=1
grownrabi=0
oldrabi=0
for month in range(1,12):
    oldrabi=oldrabi+grownrabi
    grownrabi=smallrabi
    smallrabi=oldrabi
    print("第%2d 个月，有%4d 对小兔子,%4d 对大兔子，共%4d 对兔子" %(month+1,smallrabi,grownrabi,smallrabi+grownrabi+oldrabi))
          

