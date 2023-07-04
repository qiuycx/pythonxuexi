'''
实验 7-5
生成验证码
夏帅超 2125060232
2023/5/15
'''
import random
def create(list):
    for i in range(0, 6):
        n = random.randint(0, 2)
        if (n == 0):  # 随机输出一个数字
            list.append(random.randint(0, 9))
        elif (n == 1):  # 随机输出一个字母
            list.append(chr(random.randrange(65, 90)))
        elif (n == 2):
            list.append(chr(random.randrange(97, 122)))
n = 0
list= []
create(list)
print(*list,sep='')

