#encoding: utf-8
from config import logging

def greet(name):
    def say_hello():
        nonlocal name
        name = name + ' and iris'
        print('hello {} , this is inner function'.format(name))
    return say_hello


f = greet('alex')

f()


def calculate(a,b,ope):
    if ope == 1:
        return a+b
    elif ope == 2:
        return a-b
    elif ope == 3:
        return a * b
    elif ope == 4:
        return a / b
    else:
        logging.error('No ope')

print(calculate(1,2,3))


def calculate(ope):
    def function(a,b):
        if ope == 1:
            return a+b
        elif ope == 2:
            return a-b
        elif ope == 3:
            return a * b
        elif ope == 4:
            return a / b
        else:
            logging.error('No ope')
    return function

a = calculate(3)

print(a(2,2))

def times(ope):
    def cal(x):
        return ope * (x + 1)
    return cal

b = times(3)

print(b(2))