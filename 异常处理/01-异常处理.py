from cgi import print_arguments
from tkinter import E

from numpy import isin


try:
    c = 1/0
    print(c)
except ZeroDivisionError as error:
    print("抛出异常")
    print(error)
except NameError:
    print("变量未定义ERROR")
except:
    print("抛出异常")
else:
    print("没有抛出异常")
finally:
    print("不论有无异常，都会执行")

###主动抛出异常###

def greet(name,age):
    if not isinstance(name,str):
        raise TypeError("{} must be a string type".format(name))
    if not isinstance(age,int):
        raise ArgumentError('Age must be int type')


###自定义异常###
class ArgumentError(Exception):
    def __init__(self, *args: object,**kwargs) -> None:
        super().__init__(*args,**kwargs)
        print("参数错误")

try:
    greet('alex','alex')
except Exception as err:
    print(err.args)