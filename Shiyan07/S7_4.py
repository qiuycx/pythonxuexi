'''
实验 7-4
商品筛选
夏帅超 2125060232
2023/5/15
'''
def select(list_num,list_res,min,max):
    for i in list_num:
        if  min<=i<=max:
            list_res.append(i)
def average(list_res):
    sum = 0
    for i in list_res:
        sum = sum + i
    return sum/len(list_res)

list_num = [568,239,368,425,121,219,834,1263,26]
min = eval(input("请输入区间的最小值："))
max = eval(input("请输入区间的最大值："))
list_re = []
print("排序之后的结果是：")
select(list_num,list_re,min,max)
print(list_re)
print("排序之后的结果是：")
list_re.sort()
print(list_re)
list_re.reverse()
print(list_re)
print("平均价格保留两位小数为：%.2f"%average(list_re))

