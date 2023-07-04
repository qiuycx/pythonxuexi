'''
实验1-8
冒泡排序
夏帅超 2125060232
2023/2/18
2023/2/22修改
'''
print("subject8")
ls=[23, 4, 6, 9, 2, 11, 20]
print("排序前:\n"+str(ls))
for i in range(1, len(ls)):
    for j in range(0, len(ls)-i):
        if ls[j] < ls[j+1]:
            ls[j], ls[j+1] = ls[j+1], ls[j]
print("排序后:\n"+str(ls))