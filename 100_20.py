#题目020：一个小球从100米高度自由落下，每次落地后反弹回原高度的一半，在落下，求它在第10次落地时共经历了多少米，第10次弹起的高度是多少？
#【思路分析】小球第一次经历了100米，第二次在落地时，则经历了（100/2)*2米，以此类推
'''
可以用一个变量记录每次弹起的高度
'''

distance = 0
high = 100
distance += high   #第一次着地
for i in range(9):
    high = high/2
    distance += 2*high

high=high/2
print("小球共经历了%d 米"% distance)
print("第十次再弹起，能弹%d米" % high)
