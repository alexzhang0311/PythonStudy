import logging

class Person(object):
    
    def __init__(self,name) -> None:
        self.name = name
        # self.age = 0
        # self.is_adult = False
    
    def __getattr__(self, item: str):
        '''
        __getattr__
        在访问对象不存在的属性时会调用该方法，将属性传入对象
        print(p1.name)
        print(p1.age)
        print(p1.gender)
        返回:
        alex
        __getattr__
        18
        __getattr__
        gender属性不存在
        '''
        print('__getattr__')
        if item == 'age':
            logging.warning('age 属性已经被废弃，在下一个版本中将不会使用')
            return 18
        else:
            return AttributeError(item+'属性不存在')
    
    def __getattribute__(self,item):
        '''
        __getattr__
        在访问对象时不论该属性是否存在都会调用该方法，将属性传入对象
        '''
        print('__getattribute__')
        return super(Person,self).__getattribute__(item)

    def __setattr__(self, key, value) -> None:
        '''
        __setattr__
        给一个对象属性设置值，会调用该方法。无论该属性在不在对象中
        不要使用self.xx = xxx 否则会产生递归调用,打爆内存
        p1 = Person(name='alex')
        print(p1.name)
        print(p1.age)

        p1.gender = 'Male'
        print(p1.gender)
        
        结果：
        __setattr__
        key:name,value:alex
        alex
        __getattr__
        WARNING:root:age 属性已经被废弃，在下一个版本中将不会使用
        18
        __setattr__
        key:gender,value:Male
        Male
        '''
        print('__setattr__')
        # print('key:{},value:{}'.format(key,value))
        # self.__dict__[key] = value

        if key == 'age':
            self.__dict__['age'] = value
            if self.__dict__['age'] >= 18:
                self.__dict__['is_adult'] = True
            else:
                self.__dict__['is_adult'] = False
        else:
            self.__dict__[key] = value
        
    
    # def __str__(self) -> str:
    #     return self.name

# p1 = Person(name='alex')

# print(p1.name)
# p1.age = 18
# print(p1.age)

# p1.gender = 'Male'
# print(p1.gender)

p1 = Person('alex')

p1.gender = 'Male'

p1.age = 18
print(p1.__dict__)

print(p1.exect)
###执行顺序，__setattr__ ==> __getattr__ ==> __getattribute__###