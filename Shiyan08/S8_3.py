'''
实验8-3
自定义异常类
夏帅超
2125060232
2023/5/19
'''
# 自定义异常类 OutOfStock
class OutOfStock(Exception):
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return f"Out of stock: {self.color}"


class CandleShop:
    name = "Here's a Hot Tip: Buy Drip Candles"

    def __init__(self, stock):
        self.stock = stock

    def buy(self, color):
        if self.stock[color] <= 0:
            raise OutOfStock(color)
        self.stock[color] = self.stock[color] - 1


candle_shop = CandleShop({'blue': 6, 'red': 2, 'green': 0})

try:
    candle_shop.buy('blue')
    # 这里添加代码以引发 OutOfStock 异常
    candle_shop.buy('green')
except OutOfStock as e:
    print(e)