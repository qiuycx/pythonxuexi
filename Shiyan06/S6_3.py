'''
实验6-3
创建一个保险类
夏帅超 2125060232
2023/4/10
'''
class InsurancePolicy:
  #父类保险政策类
  def __init__(self, price_of_item):
    self.price_of_item = price_of_item
class VehicleInsurance(InsurancePolicy):
  #子类交通险类
  def __init__(self, price_of_item, vehicle_Name):
    super().__init__(price_of_item)
    self.vehicle_Name=vehicle_Name
  def get_rate(self):
    return self.price_of_item*0.001
class HomeInsurance(InsurancePolicy):
  #子类家庭险类
  def __init__(self,price_of_item,member_number):
    super().__init__(price_of_item)
    self.member_number=member_number
  def get_rate(self):
    return self.price_of_item*0.00005
v1=VehicleInsurance(100000,"Car")
rate_vehicle=v1.get_rate()
print("交通险回报率为：",rate_vehicle)

h1=HomeInsurance(1000000,6)
rate_home=h1.get_rate()
print("家庭险回报率为：",rate_home)

