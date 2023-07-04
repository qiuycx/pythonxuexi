'''
实验1-6
输入一个数，判断它是奇数还是偶数
夏帅超 2125060232
2023/2/18
2023/2/22修改
'''
print("subject6")
num3=input("请输入一个非负整数:\n")
num3=int(num3)
if num3<0:
    print("请输入正确的数")
elif num3==0:
    print("该数为偶数")
elif num3==1:
    print("该数为奇数")
elif num3%2==0:
    print("该数为偶数")
elif num3%2==1:
    print("该数为奇数")