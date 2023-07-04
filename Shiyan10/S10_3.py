'''
实验10-3 根据要求完成题目
夏帅超 2125060232
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
    next(reader)  # 跳过标题行
    for row in reader:
        price = float(row[1])  # 假设价格在第二列
        prices.append(price)

prices.sort(reverse=True)
highest_price = prices[0]
lowest_price = prices[-1]
average_price = sum(prices) / len(prices)

print(f"商品的最高价格：{highest_price}")
print(f"商品的最低价格：{lowest_price}")
print(f"商品的平均价格：{average_price:.2f}")
prices = []
with open('goods.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    next(reader)  # 跳过标题行
    for row in reader:
        price = float(row[1])  # 假设价格在第二列
        prices.append(price)

plt.hist(prices, bins=10, edgecolor='black')
plt.xlabel('Price')
plt.ylabel('Count')
plt.title('Price Distribution')
plt.show()