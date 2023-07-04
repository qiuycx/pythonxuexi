'''
实验5-1
利用递归计算1到100的和
夏帅超 2125060232
2023/3/24
'''
def add1(n):
    if n==1:
        return 1
    return n+add1(n-1)
print(add1(100))
