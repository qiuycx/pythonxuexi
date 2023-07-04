'''
实验2—4
输出九九乘法表
夏帅超 2125060232
2023/3/1
'''
print("九九乘法表")
for i in range(1, 11):
    for j in range(1, i+1):
        print("%d*%d=%d\t" % (j, i, j*i), end="")
    print(" ")
