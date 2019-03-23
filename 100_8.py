#打印乘法口诀表
#【思路分析】这题是学习循环嵌套一个不错的题目
'''
对于打印输出时%的应用也非常有示范意义
'''
for i in range(1,10):
    for j in range(1,i+1):
        print("%d * %d = %d    " %( j,i,i*j),end=" ")
    print("\n")

    
