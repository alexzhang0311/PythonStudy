from binascii import crc32


class Coordinate(object):
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
    def __str__(self) -> str:
        return "(%s,%s)" % (self.x,self.y)
    
    def __iadd__(self,other):
        print('__iadd__')
        new_coordinate = Coordinate(self.x + other, self.y + other)
        return new_coordinate
    
    def __isub__(self,other):
        print('__isub__')
        new_coordinate = Coordinate(self.x - other, self.y - other)
        return new_coordinate
    
    def __imul__(self,other):
        print('__imul__')
        new_coordinate = Coordinate(self.x * other, self.y * other)
        return new_coordinate

    def __itruediv__(self,other):
        print('__itruediv__')
        new_coordinate = Coordinate(self.x / other, self.y / other)
        return new_coordinate
    


c1 = Coordinate(1,2)
c2 = Coordinate(3,4)

c1 +=1
print(c1)

c2 -= 2
print(c2)

c1 *= 2
print(c1)

c1 /= 3
print(c1)