'''
实验4—1
编写函数calcluate
接受任意多个数，返回一个元组，第一个值为所有参数的平均值
第二个值是大于平均值的所有数
夏帅超 2125060232
2023/3/14
'''
def calcluate(num_list) :
    num_list = []
    avr_list = []
    n = 0
    while True:
        user_input = input("请输入一个值，或者输入字母停止输入: ")
        if user_input.isalpha():
            break
        i=float(user_input)
        num_list.append(i)
        n += i
    n=n/len(num_list)
    avr_list.append(n)
    for j in num_list:
        if j>n:
            avr_list.append(j)
    avr_tuple=tuple(avr_list)
    return avr_tuple
num_list1=[]
print(calcluate(num_list1))
