#题目015：获取输入的内容，用条件运算符的嵌套方式来完成此题，学习成绩>=90分的同学用A表示，60-89分之间用B表示，60分以下用C表示。


score=int(input("请输入考试成绩："))
if score>=90:
    grade="A"
elif score>=60:
    grade="B"
else:
    grade="C"
print(grade)
