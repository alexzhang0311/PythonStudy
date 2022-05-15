###封装\继承\多态

###继承###
###先在子类中找方法，再从父类中找方法###

from cgi import print_arguments
from codecs import getencoder
from msilib.schema import Class


class Person(object):
    def __init__(self,name,age,gender='MALE') -> None:
        self.name = name
        self.age = age
        self.__gender = gender #私有变量,只能包在方法中访问,子类不能继承

    def info(self):
        print("姓名：{}年龄：{}性别：{}".format(self.name,self.age,self.__gender))
    
    def eat(self):
        print("{}爸爸在吃饭".format(self.name))
    
    def __run(self): #私有方法，子类无法继承
        print("{}爸爸在跑".format(self.name))

class Student(Person):
    def __init__(self, name, age, habbit, gender) -> None: #gender属于student类
        super().__init__(name, age, gender) #super(类名,self)函数返回父类的对象，执行父类的init函数，参数需要与父类保持一致
        self.habbit = habbit
    def study(self):
        print("{}开始{}!".format(self.name,self.habbit))
    ###子类方法重写，不会使用父类方法###
    def eat(self):
        print("儿子{}在吃饭".format(self.name))
        super().eat() #调用父类的方法
        #super().__run() 父类私有方法
# alex = Person(name='alex',age=18,gender='Male')
alex = Person(name='alex',age=18)
tim = Student(name='Tim',age=30,habbit='Study',gender='Famale')

tim.info()
tim.eat()
tim.study()

alex.info()

###多继承###
###一个子类同时继承两个父类###

class horse(object):
    def run(self):
        print("可以跑~")
    
    def eat(self):
        print("在吃草")

class donkey(object):
    def pull_the_grind(self):
        print("会拉磨")
    
    def eat(self):
        print("吃稻谷")

class mule(horse,donkey):
    def eat(self):
        donkey.eat(self=self)
        super().eat() #super 遵循__mro__顺序
        print("吃粑粑")

m1 = mule()
m1.run()
m1.pull_the_grind()
m1.eat()
print(mule.__mro__) ###多继承方法调用顺序###
