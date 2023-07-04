'''
实验5-3
使用闭包编写一个学生成绩平均统计，要求每次调用函数传入一个学生成绩，得到已经穿入成绩的平均分
夏帅超 2125060232
2023/3/24
'''
def avrg_score():
    scores=[]
    def inner(score):
       nonlocal scores
       scores.append(score)
       average=sum(scores)/len(scores)
       return average
    return inner
average_score=avrg_score()
print(average_score(1))
print(average_score(20))
print(average_score(50))
print(average_score(100))

