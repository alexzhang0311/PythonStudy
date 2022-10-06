
###传统动态创建类###
def create_class(name):
    if name == 'car':
        class Car():
            def run():
                print("Car is running")
        return Car
    else:
        class Person():
            def run():
                print("Person is running")
        return Person

Myclass = create_class('car')
Myclass.run()

###使用Type动态创建类###


Person = type('Person',(object,),{"name":"alex","age":"18"})

p = Person()
print(p.name)