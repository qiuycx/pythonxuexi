'''
实验2-3
阿拉伯数字转化为对应大写汉字
夏帅超 2125060232
2023/2/28
'''

abc_list = ["零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖", "拾"]
num = input("输入金额:>")
num = int(num)
ABC_list = []
for i in range(5):
    ABC_list.append(abc_list[num % 10])
    if num > 10:
        num //= 10
    else:
        break
print("汉字转换:>")
if len(ABC_list) == 1:
    print(ABC_list[0]+"圆整")
elif len(ABC_list) == 2:
    print(ABC_list[1]+"拾"+ABC_list[0]+"圆整")
elif len(ABC_list) == 3:
    print(ABC_list[2]+"佰"+ABC_list[1] + "拾" + ABC_list[0]+"圆整")
elif len(ABC_list) == 4:
    print(ABC_list[3]+"仟"+ABC_list[2]+"佰"+ABC_list[1] + "拾" + ABC_list[0]+"圆整")
elif len(ABC_list) == 5:
    print(ABC_list[4]+"萬"+ABC_list[3] + "仟" + ABC_list[2] + "佰" + ABC_list[1] + "拾" + ABC_list[0]+"圆整")