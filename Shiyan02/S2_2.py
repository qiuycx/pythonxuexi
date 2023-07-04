'''
实验1-2
输出指定范围内的斐波那契数列
夏帅超
2125060232
2023/2/24
'''

def fibonacci_range(start, end):
    fib_list = [0, 1]
    while fib_list[-1] < end:
        fib_list.append(fib_list[-1] + fib_list[-2])
    return [i for i in fib_list[0:len(fib_list)-1] if i >= start]
print("请输入两个数")
print(fibonacci_range(int(input("start:")), int(input("end:"))))
