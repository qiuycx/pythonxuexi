'''
实验5-4
编写一个装饰器，使得他呢能够打印输出所装饰函数的运算时间
夏帅超 2125060232
2023/3/24
'''
import time
def timing_decoraator(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.5f} seconds to execute.")
        return result
    return inner
@timing_decoraator
def add1(n):
    if n==1:
        return 1
    return n+add1(n-1)
print(add1(100))
