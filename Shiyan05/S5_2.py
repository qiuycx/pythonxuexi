'''
实验5-2
使用高阶函数方式设计Calc函数，实现加，减，乘，除，乘方等计算功能
夏帅超 2125060232
2023/3/24
'''
def Calc(f,x,y):
    return f(x,y)
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y!=0:
      return x/y

def power (x,y):
    return x**y
print(Calc(add,2,3))#输出5（即2+3）
print(Calc(subtract,5,1))#输出4（即5-1）
print(Calc(multiply,50,12))#输出600（即50x12）
print(Calc(divide,35,5))#输出7（即35/7）
print(Calc(power,3,4))#输出81（即3的四次方）
