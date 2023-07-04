'''
ʵ��9-1
��˧��
2125060232
2023/6/2
'''
import pymysql
import csv
# ����
conn = pymysql.connect(host='127.0.0.1', user='root', password='henu', db='test', port=3306)
cursor = conn.cursor()
cursor.execute("CREATE TABLE tb_score(sno CHAR(10) NOT NULL, name VARCHAR(20) NULL,score INT NULL, PRIMARY KEY (sno))")

ls = []
ls.append(['10001', "С��", 90])
ls.append(['10002', "С��", 85])
ls.append(['10003', "С��", 83])
ls.append(['10004', "С��", 92])
ls.append(['10005', "С��", 81])

sql = "insert into tb_score(sno,name,score) values('{0}','{1}',{2})"
try:
    for row in ls:
        cursor.execute(sql.format(*row))
    conn.commit()
except:
    conn.rollback()

# ��ӡ��������
cursor.execute("select * from tb_score")
rows = cursor.fetchall()
ls2 = list(map(list, rows))
print(ls2)

# 1
insert = ['10006', "С��", 78]
try:
    cursor.execute(sql.format(*insert))
    conn.commit()
except:
    conn.rollback()

# 2
sql = "select * from tb_score where score<{0}"
cursor.execute(sql.format(90))
rows = cursor.fetchall()
ls3 = list(map(list, rows))
print(ls3)
with open("data.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(ls3)

# 3
update = "update tb_score set sno = concat('S' , sno)"
cursor.execute(update)
conn.commit()

# 4
sql = "delete from tb_score where name='{0}'"
try:
    cursor.execute(sql.format("С��"))
    conn.commit()
except:
    conn.rollback()

cursor.close()
conn.close()

