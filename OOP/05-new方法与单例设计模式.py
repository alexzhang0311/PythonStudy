###__new__方法###
#这个方法是在对象还没有创建之前就会执行的，__init__方法是在对象创建完毕之后才会执行

class Person(object):
    def __new__(cls,*args,**kwargs):
        print("调用了__new__方法")
        print(args)
        print(kwargs)
        return super().__new__(cls) #若不加此句则__new__方法返回为空
        

    def __init__(self,name):
        self.name = name
        print("调用了__init__方法{}".format(self.name))

    

# p = Person(name='alex')
# p = Person('alex')

class Student(Person):
    def __new__(cls, *args, **kwargs):
        print("Student的new方法！")
        print(args)
        print(kwargs)
        return super(Student,cls).__new__(cls, *args, **kwargs) ###可以把参数传递给父类
    
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age
        print("调用了__init__方法{} {}".format(self.name,self.age))

Student(name='Iris',age=18)

###单例设计模式###
#控制类只有一个实例对象

class Person(object):
    __instance = None
    
    def __new__(cls,*args,**kwargs) :
        if not cls.__instance:
            print("实例不存在")
            cls.__instance = super(Person,cls).__new__(cls,*args,**kwargs)
            # return cls.__instance
        else:
            print("实例已经存在",cls.__instance)
        # print(args)
        return cls.__instance
            # print(cls.__instance)
            # return super().__new__(cls)
        # else:
        #     print("已经有了")
        #     return cls.__instance

    def showname(self,name):
        self.name = name
        print("恭喜{}，实例创建成功".format(self.name))

    @classmethod
    def get_user(cls):
        cls.name = 'alex'
        print(cls.name)

import time,threading
# def test(name):
#     p = Person()
#     p.showname(name=name)
#     print(id(p))
#     time.sleep(10)


# def writefile(name):
#     f = open('test', 'a')
#     print(f)
#     f.write(name)
#     f.close()

# t1 = threading.Thread(target=writefile, name='tim',args=('tim\n',))
# t2 = threading.Thread(target=writefile, name='alex',args=('alex\n',))

# t1.start()
# t2.start()
# t1.join()
# t2.join()

class writefile(object):
    __instance = None

    def __new__(cls,*args,**kwargs):
        if not cls.__instance:
            cls.__instance = super(writefile,cls).__new__(cls)
        return cls.__instance
    
    # def __init__(self,info) -> None:
    #     self.info = info
    def write(self,info):
        f = open('test', 'a')
        print(f)
        f.write(info)
        # time.sleep(5)
        f.close()

file = writefile()
file.write('alex\n')

# def test(info):
#     file = writefile()
#     print(id(file))
#     file.write(info)


# t1 = threading.Thread(target=test, name='tim',args=('tim\n',))
# t2 = threading.Thread(target=test, name='alex',args=('alex\n',))

# t1.start()
# # time.sleep(1)
# t2.start()
# t1.join()
# t2.join()

# t1 = threading.Thread(target=test, name='tim',args=('tim',))
# t2 = threading.Thread(target=test,name='alex',args=('alex',))
# t1.start()
# #time.sleep(1)
# t2.start()
# t1.join()
# t2.join()
# alex = Person('Alex')
#print(id(tim))
# # Person('Tim')
#print(id(alex))

# print(tim is alex)

###不是线程安全，在多线程使用下会出现并发问题，需要用到锁的机制###
