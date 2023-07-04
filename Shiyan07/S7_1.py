'''
实验7-1
实现好友管理系统
夏帅超 2125060232 2023/5/1
'''
class FriendManagementSystem:

#创建列表用于存储好友信息

    def __init__(self):
        self.friends = []

    def add_friend(self):
       # 实现添加好友功能
        friend_name=input("请输入要添加的好友:\n")
        if friend_name in self.friends:
            print("要添加的好友已存在")
        else:
            self.friends.append(friend_name)
            if friend_name in self.friends:
                print("添加成功")

    def del_friend(self):
        #实现删除好友功能
        friend_name=input("请输入要删除的好友:\n")
        if friend_name in self.friends:
            self.friends.remove(friend_name)
            if friend_name not in self.friends:
                print("删除成功")
        else:
            print("要删除的好友不存在")

    def change_friend_name(self):
        #实现修改好友功能
        friend_name1=(input("请输入要修改的好友：\n"))
        if friend_name1 in self.friends:
            friend_name2 = (input("请输入备注:\n"))
            if friend_name2 not in self.friends:
                index = self.friends.index(friend_name1)
                self.friends[index] = friend_name2
                print("备注成功")
            else:
                print("无法与已经存在的好友重复")
        else:
            print("要修改的好友不存在")

    def display_friends(self):
        #实现输出好友列表功能
        if not self.friends:
            print("好友列表为空")
        else:
            print("好友列表:")
            for friend in self.friends:
                print(friend)

    def run(self):
        while True:
            print("请选择操作")
            print("1.添加好友")
            print("2.删除好友")
            print("3.备注好友")
            print("4.展示好友")
            print("5. 退出 ")

            choice =input("请输入您的选项:\n")
            if choice=="1":
                self.add_friend()
            elif choice=="2":
                self.del_friend()
            elif choice=="3":
                self.change_friend_name()
            elif choice=="4":
                self.display_friends()
            elif choice=="5":
                print("感谢使用好友管理系统，再见！")
                break
            else:
                print("无效的选项，请输入")


FMS=FriendManagementSystem()
FMS.run()
