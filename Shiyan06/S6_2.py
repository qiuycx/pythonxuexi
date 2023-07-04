'''
实验6-2
用面向对象的方法实现带有计数器的学生类
夏帅超 2125060232
2023/3/31
'''
class Student:
    count=0#用于统计实例化学生对象数量的类属性

    def __init__(self, name):
        self.name = name
        Student.count+=1
    @staticmethod
    def get_students_count():
        return  Student.count
try:
     n=int(input("请输入学生的数量:\n"))
except ValueError:
     print("输入的数量无效，应该输入一个整数")
     exit()
students=[]#创建了一个用于储存学生对象的列表
for i in range(n):
    name1=input(f"请输入第{i+1}个学生的名字:\n")
    s=Student(name1)
    students.append(s)#将创建好的学生对象添加到列表

    #检查学生是数量是否为空
    if len(students) == 0:
        print("当前没有学生信息。")
    else:
        # 打印学生的信息以及数量
        for i, s in enumerate(students):
            print(f"第{i + 1}位学生的名字是：{s.name}")
        print(f"一共有{Student.get_students_count()}位学生。")

