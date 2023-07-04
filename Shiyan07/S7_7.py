'''
实验 7-7
删除奇数
夏帅超 2125060232
2023/5/15
'''
import random
list_num = [random.randint(0,100) for i in range(50)]
print("没有删除之前：")
print(list_num)
for i in range(49,-1,-1):
    if list_num[i] % 2 == 1:
        del list_num[i]
print("删除奇数元素之后：")
print(list_num)