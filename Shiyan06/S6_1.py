'''
实验6-1
用面向对象的方法实现大象进冰箱整个过程的基本操作
夏帅超 2125060232
2023/3/31
'''
#设大象进入冰箱的整个过程锁需要的路程为300
distance=300
class Elephant:
    def __init__(self,name,speed):
        self.name=name
        self._speed=speed
    @property
    def speed(self):
        return self._speed

    @speed.setter
    def Speed(self,value):
        if 1<=value<=80:
            self._speed=value
        else:
            raise ValueError("速度应该在1-80之间")
    def move(self):
            print(f"{self.name} 在以 {self._speed}速度移动.")
elephant1 = Elephant("Elephant 1", 50)
elephant2 = Elephant("Elephant 2", 30)
elephant3 = Elephant("Elephant 3", 70)
elephants = [elephant1, elephant2, elephant3]
elephants.sort(key=lambda e: e.Speed, reverse=True)

print("大象的名称和速度如下:")
for elephant in elephants:
    print(f"{elephant.name}: {elephant.Speed}")

elephant3.Speed = 10
elephants.sort(key=lambda e: e.Speed, reverse=True)
print("\n大象开始进入冰箱:")
for elephant in elephants:
    elephant.move()
print("大象已全部进入冰箱")
for elephant in elephants:
   time= float(distance)/float(elephant.speed)
   time=str(time)
   print(elephant.name+"用时"+time)




