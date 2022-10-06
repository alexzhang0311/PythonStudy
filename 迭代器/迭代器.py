from collections.abc import Iterable,Iterator
###判断对象是否可迭代###

ret = isinstance([1,2,3], Iterable)
print(ret)


###迭代器对象###

class MyRangeIterator(object):
    def __init__(self,start,end):
        self.index = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < self.end:
            temp = self.index
            self.index += 1
            return temp
        else:
            raise StopIteration()

###可迭代对象###  可迭代对象 + 迭代器对象的方式可以实现无限次迭代。如果只有迭代器对象，则只可以实现一次迭代
class MyRange(object):
    def __init__(self,start,end):
        self.start = start
        self.end = end
    
    def __iter__(self):
        ###返回一个迭代器对象###
        return MyRangeIterator(self.start, self.end) ###每次都调用迭代器的next方法

ret = MyRange(1, 10)
print(isinstance(ret, Iterable))
for x in ret:
    print(x)
print('xxxxxxxxxxxxxxxxxxx')
for y in ret:
    print(y)


###for 循环原理，先获取可迭代对象的迭代器，再执行迭代器的next函数
ret_iterator = iter(ret) #ret_iterator = MyRangeIterator(self.start, self.end) 
print(isinstance(ret_iterator, Iterable))
while True:
    try:
        x = ret_iterator.__next__()
        print(x)
    except StopIteration:
        break
print('------------------')

###这种方式只可以被遍历一次###
a = MyRangeIterator(1,10)
for x in  a:
    print(x)
print('******************')
for y in  a:
    print(y)


###标准的range函数可以一直被遍历###
a = range(1,3)

for x in  a:
    print(x)
print('******************')
for y in  a:
    print(y)

###只有迭代器才有next函数###
a = ['a','b']

b = iter(['a','b'])
print(next(b))
print(isinstance(a, Iterator))
print(isinstance(b, Iterator))

print(isinstance(MyRange(1,2), Iterator))
print(isinstance(MyRange(1,2), Iterable))
print(isinstance(MyRangeIterator(1,2), Iterator))
print(isinstance(MyRangeIterator(1,2), Iterable))