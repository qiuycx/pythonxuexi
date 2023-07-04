'''
S4_3
密文替换
夏帅超 2125060232
2023/3/17
'''
def num_replace(str1,mapping):
 for num,letter in mapping.items():
  str1=str1.replace(num,letter)
 return str1
str1=input("请输入密文:")
mapping={
 "0":"O",
 "1":"I",
 "2":"Z",
 "3":"E",
 "4":"Y",
 "5": "S",
 "6": "G",
 "7": "L",
 "8": "B",
 "9": "P",
}
str2=num_replace(str1,mapping)
print(str2)