class Coordinate(object):
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
    def __pos__(self):
        print("__pos__")
        '''
        在对象前面有+时会调用
        print(+c1)
        结果：
        __pos__
        (-1,-2)
        '''
        return self
    def __neg__(self):
        print("__neg__")
        '''
        在对象前面有-时会调用
        创建一个对象新的副本，不会改变对象本身
        c1 = Coordinate(-1,-2)
        print(c1)

        c2 = -c1

        print(c1)
        print(c2)
        结果：
        (-1,-2)
        __neg__
        (-1,-2)
        (1,2)
        '''
        new_coordinate = Coordinate(-self.x,-self.y)
        return new_coordinate
        '''
        会改变对象本身
        c1 = Coordinate(-1,-2)
        print(c1)

        c2 = -c1

        print(c1)
        print(c2)
        结果：
        (-1,-2)
        __neg__
        (1,2)
        (1,2)
        '''
        # self.x = -self.x
        # self.y = -self.y
        # return self

    def __abs__(self):
        print("__abs__")
        '''
        在对象前面有abs时会调用
        '''
        new_coordinate = Coordinate(abs(self.x),abs(self.y))
        return new_coordinate

    def __invert__(self):
        print("__invert__")
        '''
        在对象前面有~时会调用
        '''
        new_coordinate = Coordinate(255-self.x,255 - self.y)
        return new_coordinate

    def __str__(self) -> str:
        return "(%s,%s)" % (self.x,self.y)


c1 = Coordinate(-1,-2)
# print(+c1)
# print(c1)

c2 = -c1

print(c1)
print(c2)
print(abs(c1))
print(~c1)