login_info = {'login_status':True}


def test():
    def edit_user():
        if login_info['login_status'] == True:
            print('edit user success')
        else:
            print('Please Login!')
    
    def add_article():
        if login_info['login_status'] == True:
             print('add article success')
        else:
            print('Please Login!')
    
    edit_user()

test()

def test01():
    def login_required(func):
        if login_info['login_status'] == True:
            func()
        else:
            print('Please Login!')
    
    def edit_user():
        print('edit user success')
    
    def add_article():
        print('add article success')

    login_required(edit_user)

test01()

def test02():
    def login_required(func):
        def wrapper():
            if login_info['login_status'] == True:
                func()
            else:
                print('Please Login')
        return wrapper
    
    def edit_user():
        print('edit user success')
    
    def add_article():
        print('add article success')
    
    login_required(edit_user)()

test02()

def test03():
    def login_required(func):
        def wrapper():
            if login_info['login_status'] == True:
                func()
            else:
                print('Please Login')
        return wrapper
    
    @login_required
    def edit_user():
        print('edit user success')
    
    @login_required
    def add_article():
        print('add article success')
    
    add_article()

test03()

import time

def timer(func):
    def wrapper():
        start = time.time()
        n = 0
        while 1:
            print(n)
            time.sleep(1)
            if time.time() - start >= 3:
                print('function overtime')
                break
            else:
                func()
                n += 1
    return wrapper


class test04(object):
    __instance = None
    def __init__(self):
        pass
    def __new__(cls,*args,**kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    #@timer
    def count(self):
        print('a')

@timer
def count():
    print('a')


###被装饰器装饰的函数需要传递参数###
def login_required(func):
        def wrapper(username):
            if login_info['login_status'] == True:
                func(username)
            else:
                print('Please Login')
        return wrapper

@login_required #login_required(edit_user) == wrapper
def edit_user(username=None):
    print('edit user %s success' % username)

@login_required
def add_article():
    print('add article success')

edit_user('alex')

def login_required(func):
        def wrapper(*args,**kwargs):
            if login_info['login_status'] == True:
                print(*args,'*agrs')
                print(args,'agrs')
                print(kwargs)
                func(*args,**kwargs)
            else:
                print('Please Login')
        return wrapper

@login_required #login_required(edit_user) == wrapper
def edit_user(username,age):
    print('edit user {} success age {}'.format(username,age))

@login_required
def add_article():
    print('add article success')

edit_user('alex',19)
edit_user(username='alex',age=19)


###给装饰器传递###

def login_required(site='front'):
    def outterwrapper(func):
        def innerwrapper(*args,**kwargs):
            if login_info['login_status'] == False:
                func(*args,**kwargs)
            else:
                if site == 'front':
                    print('返回前端')
                else:
                    print('返回后端')
        return innerwrapper
    return outterwrapper



@login_required('front')
def edit_user(username,age):
    print('edit user {} success age {}'.format(username,age))

edit_user('tim',21)


### wrap 装饰器 ###


def great(func):
    def wrapper(*args,**kwargs):
        print('闭包开始')
        func(*args,**kwargs)
        print('闭包结束')
    return wrapper

@great
def hello(name):
    print('hello %s' % name)

hello('alex')

print('函数名称',hello.__name__) #加了装饰器之后，函数的名字变为wrapper，所以需要warps


from functools import wraps

def great(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print('闭包开始')
        func(*args,**kwargs)
        print('闭包结束')
    return wrapper

@great
def hello(name):
    print('hello %s' % name)

hello('alex')

print('函数名称',hello.__name__) #加了装饰器之后，函数的名字变为wrapper，所以需要warps




def test():
    a = 'hello alex'
    return a



def login_required(func):
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs)
    return wrapper

@login_required
def test(name):
    a = 'hello {}'.format(name)
    return a

a = test('alex')

print(a)