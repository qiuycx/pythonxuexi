'''
实验3-1
提取所有学生的姓名，序号，成绩。
夏帅超 2125060232
2023/3/3
'''
str1 = '''<tbody>
<tr><td><span><span class="c-index  c-index-hot1 c-gap-icon-right-small">1</span>张婷婷</span></td><td class="opr-toplist-right">92<i class="opr-toplist-st c-icon c-icon-down"></i></td></tr>
<tr><td><span><span class="c-index  c-index-hot2 c-gap-icon-right-small">2</span>王华</span></td><td class="opr-toplist-right">91<i class="opr-toplist-st c-icon c-icon-down"></i></td></tr>
<tr><td><span><span class="c-index  c-index-hot3 c-gap-icon-right-small">3</span>张岚</span></td><td class="opr-toplist-right">90<i class="opr-toplist-st c-icon c-icon-down"></i></td></tr>
<tr><td><span><span class="c-index  c-gap-icon-right-small">4</span>孙鸿峰</span></td><td class="opr-toplist-right">90<i class="opr-toplist-st c-icon c-icon-down"></i></td></tr>
<tr><td><span><span class="c-index  c-gap-icon-right-small">5</span>周海栋</span></td><td class="opr-toplist-right">89<i class="opr-toplist-st c-icon c-icon-down"></i></td></tr>
<tr><td><span><span class="c-index  c-gap-icon-right-small">6</span>武静</span></td><td class="opr-toplist-right">88<i class="opr-toplist-st c-icon c-icon-down"></i></td></tr>
</tbody>'''
s = str1.split("</tr>")
str2 = "序号:{0} 姓名:{1} 成绩:{2}"
sno_list = []
name_list = []
score_list = []
for i in range(6):
    start1 = int((s[i].find('small">')))+len('small">')#find函数用来查找子串是否在字符串中，如果在则返回子串位置下标，否则返回-1
    end1 = int((s[i].find("</span>")))
    sno_list.append(s[i][start1:end1])
    start2 = int((s[i].find("</span>")))+len("</span>")
    end2 = int((s[i]).find("</span></td>"))
    name_list.append(s[i][start2:end2])
    start3 = int((s[i].find('<td class="opr-toplist-right">')))+len('<td class="opr-toplist-right">')
    end3 = int((s[i]).find('<i class="opr-toplist-st c-icon c-icon-down">'))
    score_list.append(s[i][start3:end3])#append函数用来在列表最后加上新值
    print(str2.format(sno_list[i], name_list[i], score_list[i]))#使用按位置参数对字符串进行格式化输出。
