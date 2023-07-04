'''
实验2-7
计算BMI数值
夏帅超 2125060232
2023/3/1
'''
height = float(input("请输入身高（单位:m）:"))
weight = float(input("请输入体重（单位:kg）:"))
BMI = (weight/(height*height))
if BMI < 18.5:
    print("过轻")
elif 18.5 <= BMI < 24:
    print("正常")
elif 24 <= BMI < 27:
    print("过重")
elif 27 <= BMI < 32:
    print("肥胖")
elif BMI > 32:
    print("非常肥胖")
