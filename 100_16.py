#问题016：关于时间及日期的格式的诸多表示方法

import time
print(time.time())           #打印出来是时间戳
print(time.localtime())      #时间元组，注意:tm_wday中0是周一
print(time.asctime())        #以ASC码的形式来输出时间，即可读的文本形式
print(time.strftime('%Y-%m-%d  %H:%M:%S',time.localtime()))#把时间格式转为字符

st = time.localtime(time.time())
date = time.strftime('%Y-%m-%d',st) #只取日期，注意大小为指定的
print(date)

import datetime
dt1 = datetime.datetime.fromtimestamp(123411111)#随意输入的一串十位数
print(dt1,type(dt1))
dt2 = datetime.datetime.now()
print(dt2)
print('相差%d天，零%.1f个小时'%((dt2-dt1).days,(dt2-dt1).seconds/60/60))
