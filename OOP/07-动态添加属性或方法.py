class Person():
    country = 'USA'
    def __init__(self,name):
        self.name = name

p = Person('Alex')
p.age = 18
setattr(p, 'gender', 'Male')

print(p.name,p.age,p.gender)

###判断是否存在某属性###

print(hasattr(p, 'age'))


###动态添加实例方法###
import types
def run(self):
    print('%s 在奔跑' %self.name)


p.run = types.MethodType(run, p)

p.run()

###动态添加类方法###
@classmethod
def immgrate(cls):
    print('Alex将会移民到 %s' %cls.country)

Person.immgrate = immgrate

p.immgrate()

###动态添加静态方法###
@staticmethod
def static():
    print('静态方法不需要任何参数')

p.static = static

p.static()

###动态删除属性和方法###

print(p.name)

# del p.name
delattr(p, 'name')
# print(p.name)

###__slot__魔术变量###
###指定类里面只可以添加某些属性###


class Person(object):
    __slots__=('name','age')
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
p = Person('alex', 29)

setattr(p,'Gender', 'Male')
print(p.Gender)
