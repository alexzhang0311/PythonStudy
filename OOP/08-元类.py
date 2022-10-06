###在python中，一切对象皆是类###

###元类 ==> 类对象 ==> 普通对象(实例)###
###type是所有类对象的默认元类###

age = 35
print(age.__class__)
print(age.__class__.__class__)

name = 'alex'
print(name.__class__)
print(name.__class__.__class__)

def foo():
    pass

print(foo.__class__)
print(foo.__class__.__class__)

class Person():
    pass

print(Person.__class__) ###返回type###

person = Person()

print(person.__class__)

###__metaclass__为创建的类对象指定元类，默认为type###
###自定义元类###

class UpperAttrsMetaClass(type):
    def __new__(cls, class_name,parents,class_attrs):
        new_attrs = [(k,v) for k,v in class_attrs.items() if not k.startswith("__") and not k.endswith("__")]
        upper_attrs = dict((k.upper(),v) for k,v in new_attrs)
        return super(cls, UpperAttrsMetaClass).__new__(cls, class_name,parents,upper_attrs)

class Person(object,metaclass=UpperAttrsMetaClass):
    country = 'china'

p = Person()

print(p.COUNTRY)

