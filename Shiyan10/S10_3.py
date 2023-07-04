'''
ʵ��10-3 ����Ҫ�������Ŀ
��˧�� 2125060232
2023/6/12
'''
import csv
import matplotlib.pyplot as plt
with open('goods.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
prices = []
with open('goods.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    next(reader)  # ����������
    for row in reader:
        price = float(row[1])  # ����۸��ڵڶ���
        prices.append(price)

prices.sort(reverse=True)
highest_price = prices[0]
lowest_price = prices[-1]
average_price = sum(prices) / len(prices)

print(f"��Ʒ����߼۸�{highest_price}")
print(f"��Ʒ����ͼ۸�{lowest_price}")
print(f"��Ʒ��ƽ���۸�{average_price:.2f}")
prices = []
with open('goods.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    next(reader)  # ����������
    for row in reader:
        price = float(row[1])  # ����۸��ڵڶ���
        prices.append(price)

plt.hist(prices, bins=10, edgecolor='black')
plt.xlabel('Price')
plt.ylabel('Count')
plt.title('Price Distribution')
plt.show()