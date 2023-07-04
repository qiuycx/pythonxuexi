'''
实验10-1
根据示例创建ndarray，并按要求完成操作
夏帅超 2125060232
2023/6/12
'''

import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.family'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
x = np.linspace(-10,10,50)
y = x ** 6
plt.plot(x,y,'ro-')
plt.title("抛物线")
plt.xlabel("x tick")
plt.ylabel("voltage")
plt.show()
