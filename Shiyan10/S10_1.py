'''
ʵ��10-1
����ʾ������ndarray������Ҫ����ɲ���
��˧�� 2125060232
2023/6/12
'''

import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.family'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
x = np.linspace(-10,10,50)
y = x ** 6
plt.plot(x,y,'ro-')
plt.title("������")
plt.xlabel("x tick")
plt.ylabel("voltage")
plt.show()
