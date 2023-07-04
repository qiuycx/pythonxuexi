import csv
# 以字典格式读取CSV文件并打印每个人的名字和电子邮件地址
with open('user.csv', 'r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row['name']
        email = row['email']
        print(f"Name: {name}, Email: {email}")
with open('user.csv', 'r', newline='') as read_file:
    reader = csv.reader(read_file)
    rows = list(reader)

with open('usercopy.csv', 'w', newline='') as write_file:
    writer = csv.writer(write_file)
    writer.writerows(rows)