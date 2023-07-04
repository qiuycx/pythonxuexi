'''
实验7-2
实现中文数字对照表
夏帅超 2125060232
2023/5/12
'''
def exchange(list1,list2,num):
    for i in num:
        list2.append(list1[int(i)])
list1=['零','壹','贰','叄','肆','伍','陆','柒','捌','玖']
list2=[]
num=input("请输入你想要转换的数：\n")
exchange(list1,list2,num)
print(*list2,sep='')
