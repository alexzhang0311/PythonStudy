import sys
class Person(object):
    def __init__(self) -> None:
        self.name = 'alex'
        print("这是构造函数")
        self.fp = open('xx.txt','w')
    
    def greet(self):
        print("hello {}".format(self.name))

    def write(self,message):
        self.fp.write(message)
    
    ###内存释放前会调用的函数###
    def __del__(self):
        print("这是析构函数")
        self.fp.close()

p = Person()
p.greet()
print(sys.getrefcount(p))
# p.write('hello alex')


# def test():
#     print("hello")

# a = test()
# print(sys.getrefcount(a))