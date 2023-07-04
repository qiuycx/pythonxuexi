'''
S7-3
学生成绩管理
夏帅超 2125060232
2023/5/12
'''
class student:
    def __init__(cls,name,score):
        cls.name = name
        cls.score = score
    def __str__(self):
        return "[name : %s,score : %d]"%(self.name,self.score)

stu1 = student("张三",100)
stu2 = student("李四",99)
stu3 = student("王五",98)
stu4 = student("赵六",97)
list_stu = []
list_stu.append(stu3)
list_stu.append(stu1)
list_stu.append(stu4)
list_stu.append(stu2)
print("学生没有按成绩排序前：")
for n in list_stu:
    print(n)
print("学生按成绩排序后：")
list_re1 = sorted(list_stu,key=lambda student:student.score,reverse=True)
for n in list_re1:
    print(n)
print("学生按成绩排序后删除最高低分并反转输出：")
del list_re1[0]
del list_re1[len(list_re1) - 1]
list_re2 = list_re1.copy()
list_re2.reverse()
for n in list_re2:
    print(n)
