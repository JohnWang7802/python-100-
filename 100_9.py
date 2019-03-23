#题目009：暂停一秒输出；
#【思路分析】相当于scratch里的等待。在有大段内容输出时，等待会有很好的显示效果；
'''
我们用一段字典的打印做例子，输出过程，方便单词记忆
'''
import time

a={"episode":"情节，插曲",
   "anecdote":"轶事，奇闻"}
for key,value in dict.items(a):
    print(key,value)
    time.sleep(1)
