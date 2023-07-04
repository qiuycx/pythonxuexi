# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
'''
author:Shuaichao Xia
Student ID:2125060232
Created Date：2023/2/18
'''
print("Created by Shuaichao Xia 2125060232")
print("subject8")
ls=[23,4,6,9,2,11,20]
print("排序前:\n"+str(ls))
for i in range(1,len(ls)):
        for j in range(0,len(ls)-i):
            if ls[j] < ls[j+1]:
                ls[j],ls[j+1] = ls[j+1],ls[j]
print("排序后:\n"+str(ls))
'''
print("sbuject7")
n=input("请输入一个非负整数:\n")
n=int(n)
if n<0:
    print("请输入一个正确的数")
elif n==0:
    print("0的阶乘为1")
else:
    i,sum=1,1
    while i<=n:
        sum*=i
        i+=1
    print(str(n)+"的阶乘为"+str(sum))
'''
'''
print("subject5")
s2="  "
print("两全"+s2+"美\n   乐 \n   无 \n   穷 ")
s2=input("请输入正确的汉字，使横竖均为成语:\n")
print("两全"+s2+"美\n   乐 \n   无 \n   穷 ")
'''



