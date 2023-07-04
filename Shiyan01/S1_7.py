'''
实验1-7
输入一个数，求他的阶乘
夏帅超 2125060232
2023/2/18
2023/2/22修改
'''
("sbuject7")
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