'''
__str__方法:
1. 在打印某个对象的时候，会调用这个对象的'__str__'方法，打印这个方法的返回值
2. 如果在使用str()函数时候，也会调用str方法
'''
class Person(object):
    def __init__(self,name) -> None:
        self.name = name
    def __str__(self) -> str:
        return 'My name is {}'.format(self.name)


p1 = Person('alex')
p2 = Person('tim')

print(p1)
print(p2)

print(str(p1))


'''
__repr__方法:
1. 在python终端中编码，使用repr方法可以显示出类名Person<zhangchi>而不是机器语言<__main__.Person object at 0x000001C31B971AC8>
2. 若对象在列表或者元祖中，并且该列表，元祖被打印，那么也会显示类名[Person<zhangchi>, Person<yanghan>],否则会打印[<__main__.Person object at 0x00000207F6411D68>, <__main__.Person object at 0x00000207F63FC0B8>]。__str__魔术方法无法实现
'''

class Person(object):
    def __init__(self,name) -> None:
        self.name = name
    def __repr__(self) -> str:
        return 'Person<{}>'.format(self.name)

p1 = Person('zhangchi')
p2 = Person('yanghan')


print(p1)
print(p1.name)
print([p1,p2])


'''
__dir__
1. 获取该实例中所有用户自定义的属性，以及属性对应的值,{'name': 'alex', 'age': 30, 'country': 'china'}
2. dir函数返回的是对象上拥有的所用属性，用户定义和内置属性，并且不会获取属性的值.['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age', 'country', 'name']

'''

class Person(object):
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
        self.country = 'china'

p1 = Person('alex',30)

###获取实例中的全部属性###
print(dir(p1)) 
print(p1.__dict__) 