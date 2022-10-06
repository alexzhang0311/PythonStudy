'''
__str__方法:
1. 在打印某个对象的时候，会调用这个对象的'__str__'方法，打印这个方法的返回值
2. 如果在使用str()函数时候，也会调用str方法
'''

from unicodedata import name


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

'''