###多态的好处就是，当我们需要传入xiangyu,chengyaojin时，我们只需要接收hero类型就可以了，因为xiangyu,chengyaojin都是hero类型，然后，按照hero类型进行操作即可。由于hero类型有stroke()方法，因此，传入的任意类型，只要是hero类或者子类，就会自动调用实际类型的stroke()方法，这就是多态的意思###


class hero(object):
    def __init__(self) -> None:
        pass
    def stroke(self):
        pass

class chengyaojin(hero):
    def stroke(self):
        print("程咬金的大招~~回血！")

class xiangyu(hero):
    def stroke(self):
        print("项羽的大招~~推人！")
    
# value = input("请选择英雄:\n")

# if value == '1':
#     hero = chengyaojin()
# else:
#     hero = xiangyu()

# hero.stroke()


###鸭子模型###
###只要传入的对象有stroke()大招这个方法就可以用choose这个函数，而不需要担心其类型
def choose(player):
       player.stroke()

p1 = xiangyu()
choose(p1)

p2 = chengyaojin()
choose(p2)

choose(xiangyu())
choose(chengyaojin())