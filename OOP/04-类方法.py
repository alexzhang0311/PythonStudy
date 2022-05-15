class Person(object):
    ###实例属性###
    def __init__(self) -> None:
        self.country = 'China'
    ###类属性###
    country = 'China'
    ###实例方法的第一个参数必须是self###
    def eat(self):
        print("我爱吃")
    ###类方法第一个参数必须是当前类###
    @classmethod
    def greet(cls):
        cls.country = 'USA'
        print("类方法是这样写的{}".format(cls.country))
    ###静态方法，不需要传递对象或者参数，就像普通函数一样使用。可以通过类名或者对象来调用###
    @staticmethod
    def static_method():
        print("我是静态方法")

###实例方法调用###
p1 = Person()
p1.eat()
# p1.greet()

###类方法调用###
print(Person.country)
Person.greet()
print(Person.country)

