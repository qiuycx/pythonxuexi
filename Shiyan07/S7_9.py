'''
实验 7-9
字典存储数据
夏帅超 2125060232
2023/5/15
'''
stu_list = []
stu_dict1 = {'名字':'zs','年龄':18,'成绩':97}
stu_list.append(stu_dict1)
stu_dict2 = {'名字':'ls','年龄':19,'成绩':92}
stu_list.append(stu_dict2)
stu_dict3 = {'名字':'ww','年龄':18,'成绩':93}
stu_list.append(stu_dict3)
stu_dict4 = {'名字':'zl','年龄':18,'成绩':87}
stu_list.append(stu_dict4)
print('原来学生信息顺序为：')
print('名字'+' '+'年龄'+' '+'成绩')
for x in stu_list:
    print(x['名字']+'   '+str(x['年龄'])+'  '+str(x['成绩']))
score_list = []
stu_list1 = sorted(stu_list,key=lambda x : x['成绩'],reverse=True)
print('排序后学生信息顺序为：')
print('名字'+' '+'年龄'+' '+'成绩')
for x in stu_list1:
    score_list.append(x['成绩'])
    print(x['名字']+'   '+str(x['年龄'])+'  '+str(x['成绩']))
print('学生平均成绩为：',sum(score_list)/len(score_list))

