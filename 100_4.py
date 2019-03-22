#题目004：输入某年某月某日，判断这一天是这一年的第几天？
#【程序分析】虽然python有时间模块，可以通过调用tm_yday属性很方便的得到结果，但这个函数毕竟
#记忆还是有难度的，而且这样也就失去了编程的乐趣。
'''
由于每个月份的天数都是基本固定的，这题可以用元组的概念，在闰年的2月加上1天就可以了
'''

year = int(input('请输入年份：\n'))
month = int(input('请输入月份：\n'))
day = int(input('请输入日期：\n'))

months = (0,31,59,90,120,151,181,212,243,273,304,334)

if 0 < month <=12:
    sum = months[month-1]
else:
    print("月份数不合理")
    
sum = day + sum
leap = 0
if year % 400 ==0 or ( year % 4 == 0 and year % 100 !=0):
    leap =1
if leap == 1 and month > 2:
    sum = sum +1
print("这是"+ str(year)+"年的第"+str(sum)+"天")

      
