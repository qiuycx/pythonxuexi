'''
实验3-3
分别使用位置参数，关键字参数名称，映射-列表，映射-字典实现字符串格式化输出指定内容
夏帅超 2125060232
2023/3/3
'''
str2="{0}的学号是{1}，{0}的成绩为{2}分"
str3="{name}的学号是{sno}，{name}的成绩为{score}分"
ls=["张三", "1101", 90.65]
dict1 = {"name":"张三", "sno":"1101","score":90.65}
print(str2.format("张三", "1101", 90.65))#位置参数
print(str3.format(name="张三", sno="1101" , score=90.65))#关键字参数名称
print(str2.format(*ls))#映射—列表
print(str3.format(**dict1))#映射——字典