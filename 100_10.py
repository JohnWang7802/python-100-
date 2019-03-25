#问题010：按照年月日时分秒的形式打印出当前时间，等待一秒后继续打印
#【思路分析】继续学习time模块里的属性
'''
time.localtime()获取当前时间，time.strftime()把时间型变量变成字符串
'''

import time
for a in range(10):
    print(time.strftime('今天是：%Y-%m-%d ，现在是%H:%M:%S',time.localtime(time.time())))
    time.sleep(1)
