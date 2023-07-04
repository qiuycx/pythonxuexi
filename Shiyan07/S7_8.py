'''
实验 7-8
统计词频
夏帅超 2125060232
2023/5/15
'''
count = 0
count1 = 0
count2 = 0
flag = 0#设置一个flag用来标记空格是否值出现一次
string = "who have an apple apple is free free is money you know"
for s in string:
    if(("a" <= s and s <= "z") or ("A" <= s and s <= "Z")):
        flag = 0
    else:
        if(flag == 0):
            count += 1
            flag = 1
print("单词个数为：%s"%(count + 1))

