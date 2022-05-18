###__new__方法###
#这个方法是在对象还没有创建之前就会执行的，__init__方法是在对象创建完毕之后才会执行

from matplotlib.pyplot import cla


class Person(object):
    def __new__(cls,*args,**kwargs):
        print("调用了__new__方法")
        print(args)
        print(kwargs)
        return super().__new__(cls) #若不加此句则__new__方法返回为空
        

    def __init__(self,name):
        self.name = name
        print("调用了__init__方法{}".format(name))

    

# p = Person('alex')

class Student(Person):
    def __new__(cls, *args, **kwargs):
        print("Student的new方法！")
        return super().__new__(cls, *args, **kwargs) ###可以把参数传递给父类
    
    def __init__(self, name,age):
        super().__init__(name)
        self.age = age
        print("调用了__init__方法{}".format(self.name))

Student(name='Iris',age=18)

###单例设计模式###
#控制类只有一个实例对象

class Person(object):

    __instance = None
    
    def __new__(cls,*args,**kwargs) :
        if not cls.__instance:
            # print("还没有")
            cls.__instance = super().__new__(cls)
        return cls.__instance
            # print(cls.__instance)
            # return super().__new__(cls)
        # else:
        #     print("已经有了")
        #     return cls.__instance

    def __init__(self,name):
        print("恭喜{}，实例创建成功".format(name))

    @classmethod
    def get_user(cls):
        cls.name = 'alex'
        print(cls.name)


Person('Tim')
Person('Alex')
Person.get_user()

###不是线程安全，在多线程使用下会出现并发问题，需要用到锁的机制###