class Coordinate(object):
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
    def __str__(self) -> str:
        return "(%s,%s)" % (self.x,self.y)
    
    def __add__(self,other):
        print('__add__')
        new_coordinate = Coordinate(self.x + other.x,self.y + other.y)
        return new_coordinate
    
    def __sub__(self,other):
        print('__sub__')
        new_coordinate = Coordinate(self.x - other.x,self.y - other.y)
        return new_coordinate

    def __mul__(self,other):
        print('__mul__')
        new_coordinate = Coordinate(self.x * other.x,self.y * other.y)
        return new_coordinate
    
    def __floordiv__(self,other):
        '''
        取整除：向下取整数
        '''
        print('__floordiv__')
        new_coordinate = Coordinate(self.x // other.x,self.y // other.y)
        return new_coordinate
    
    def __truediv__(self,other):
        '''
        除
        '''
        print('__truediv__')
        new_coordinate = Coordinate(self.x / other.x,self.y / other.y)
        return new_coordinate

    def __mod__(self,other):
        print('__mod__')
        new_coordinate = Coordinate(self.x % other.x,self.y % other.y)
        return new_coordinate


c1 = Coordinate(1,2)
c2 = Coordinate(3,4)
c3 = c1 + c2
print(c3)

print(c2 - c1)

print(c1 * c2)

print(c1 / c2)
print(c1 // c2)

print(c1 % c2)