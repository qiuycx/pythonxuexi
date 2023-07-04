'''
实验2-1
实现用户登录功能
夏帅超 2125060232
2023/2/24
'''
ID="admin"
PW="123"
for i in range(3):
    ID1 = input("请输入账号:")
    PW1 = input("请输入密码:")
    if  not ID1==ID or not PW1==PW:
        if(i==2):
            print("输入次数超过限制，请明天再试")
        else:
            print("输入错误，还有%s次机会"%str(2-i))
    else :
        print(" 欢迎admin")
        break