'''
实验4——2：
编写一个函数，接收字符串参数返回一个元组，元组的第一个值为大写字母的个数
第二个值为小写字母的个数、
夏帅超 2125060232
2023/3/17
'''
def s4_2(str1):
    m,n=0,0
    for s in str1:
        i = s.isupper()
        j = s.islower()
        if i:
            m += 1
        if j:
            n += 1
    return m, n
str2="ehllo WROLD"
print(s4_2(str2))