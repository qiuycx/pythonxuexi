'''
实验6-4
创建一个学生类并完成相关操作
夏帅超 2125060232
2023/4/10
'''
class Grade:
    #成绩类
    passing=60
    def __init__(self,score):
        self.score=score
    def is_passing(self):
       if self.score>=self.passing:
           return True
       return False
class Student:
    #学生类
    def __init__(self,name,year):
        self.name=name
        self.year=year
        self.grades=[]
    def add_grade(self,grade):
        if isinstance(grade,Grade):
            self.grades.append(grade)
            print("添加成功")
        else:
            print("参数类型错误，无法添加")
    def get_average(self):
        if len(self.grades)>0:
            total = sum(grade.score for grade in self.grades)
            average = total / len(self.grades)
            return average
        else:
            return 0

s1=Student("Jerry","五年级")#创建一个对象：Jerry，5年级。
try:
    n=int(input("请输入成绩的数量:\n"))
except ValueError:
    print("输入的数量不对，应为一个整数")
    exit()
for i in range(n):
    grade=int(input(f"请输入第{i+1}个科目的成绩：\n"))
    g1=Grade(grade)
    s1.add_grade(g1)

for grade in s1.grades:
    print(grade.score)
   # 判断Jerry是否有不及格成绩。
if any(not grade.is_passing() for grade in s1.grades):
    print(f"{s1.name} 有不及格成绩")
else:
    print(f"{s1.name} 没有不及格成绩")
    #输出Jerry的平均成绩
print(f"平均成绩为：{s1.get_average()}")