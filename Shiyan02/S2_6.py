'''
实验2-6
求出2-1000内的回文素数
夏帅超 2125060232
2023/3/1
'''
for i in range(2, 1001):
    star = 0
    for j in range(2, i):
        if i % j == 0:
            star = 1
    if star == 0:#筛选出2-1000内的所有素数
        s1 = str(i)
        s2 = s1[::-1]
        if s1 == s2:
            print(s1, end=" ")
