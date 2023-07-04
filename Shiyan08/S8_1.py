'''
实验8-1：文件读取
夏帅超 2125060232
 2023/5/19
'''
# 打开文件并读取内容
with open('StudentInfo.txt', 'r') as file:
    lines = file.readlines()

student_list = []  # 存储学生信息的列表

# 解析每行数据并存储为字典
for line in lines:
    line = line.strip()  # 去除行尾的换行符
    student_data = line.split(',')  # 使用逗号分隔每个字段

    # 创建字典并添加到列表中
    student_dict = {
        '学号': student_data[0],
        '姓名': student_data[1],
        '平时成绩': student_data[2],
        '期末成绩': student_data[3]
    }
    student_list.append(student_dict)

# 输出结果
for student in student_list:
    print(student)