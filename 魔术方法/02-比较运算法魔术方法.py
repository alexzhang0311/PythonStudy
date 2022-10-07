
from turtle import heading


class Person(object):
    def __init__(self,name,age,height) -> None:
        self.name = name
        self.age = age
        self.height = height
    def __eq__(self, __o: object) -> bool:
        print('__eq__方法')
        '''
        __eq__:
        拥有比较两个对象是否相等的能力
        '''
        # if self.age == __o.age and self.height == __o.height:
        #     return True
        # else:
        #     return False
        return True if self.age == __o.age and self.height == __o.height else False

    def __ne__(self, __o: object) -> bool:
        print('__ne__方法')
        '''
        __eq__:
        拥有比较两个对象是否不相等的能力
        '''
        return False if self.age == __o.age and self.height == __o.height else True

    def __lt__(self, __o: object) -> bool:
        print('__lt__方法')
        if self.age < __o.age:
            if self.age == __o.age:
                return False
            else:
                return True if self.height < __o.height else False
        else:
            return False
    
    def __gt__(self, __o: object) -> bool:
        print('__gt__方法')
        if self.age > __o.age:
            if self.age == __o.age:
                return False
            else:
                return True if self.height > __o.height else False
        else:
            return False

    def __le__(self, __o: object) -> bool:
        print('__le__方法')
        if self.__le__ or self.__eq__:
            return True
        else:
            return False

    def __ge__(self, __o: object) -> bool:
        print('__ge__方法')
        if self.__ge__ or self.__eq__:
            return True
        else:
            return False
    

p1 = Person('alex',29,182)
p2 = Person('tim',30,183)

if p1 == p2:
    print('两个对象身高体重相等')
else:
    print('两个对象身高体重不相等')


if p1 != p2:
    print('两个对象身高体重不相等')
else:
    print('两个对象身高体重相等')


if p1 < p2:
    print(True)
else:
    print(False)

if p2 > p1:
    print(True)
else:
    print(False)


p1 = Person('alex',30,183)
p2 = Person('tim',30,183)
if p2 >= p1:
    print(True)
else:
    print(False)