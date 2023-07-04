'''
实验 7-6
随机数列表
夏帅超 2125060232
2023/5/15
'''
import random
list = [random.randint(1,100) for i in range(20)]
print("排序前：")
print(list)
list1 = list[1::2]
list1.sort(reverse=True)
n = 0
for i in range(20):
    if i % 2 == 1:
        list[i] = list1[n]
        n += 1
print("对偶数下标排序后：")
print(list)



