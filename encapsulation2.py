#encapsulation program
class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age

    def get_age(self):
        return self.__age
    def set_age(self,age):
        if age>0:
            self.__age=age
        else:
            print("invalid age")

    def display(self):
        print(f"name:{self.name},Age:{self.__age}")

s1=Student("abc",21)
print(s1.name)
print("age:",s1.get_age())
s1.display()

#normal encapsulation
class Person:
    def __init__(self):
        self.__name=" "

    def setter(self,val):
        self.__name=val

    def getter(self):
        return self.__name

p1=Person()
p1.setter("rvi")
res=p1.getter()
print(res)

#property function encapsulatioin
class Laptop:
    def __init__(self):
        self.__brand=""

    def getter(self):
        return self.__brand

    def setter(self,val):
        self.__brand=val

    getset=property(getter,setter)

l1=Laptop()
l1.getset="hp"
res=l1.getset
print(res)

#@property decorator in encapsulation
class Car:
    def __init__(self):
        self.__brand=""

    @property
    def dataAccess(self):
        return self.__brand
    @dataAccess.setter
    def dataAccess(self,val):
        self.__brand=val
c1=Car()
c1.dataAccess="Audi"
res=c1.dataAccess
print(res)

#converting public method to private method in encapsulation
class Bike:
    def __init__(self):
        self.name="herohonda"
    def __move(self):
        print("car is  moving")
    def helper(self):
        self.__move()

b1=Bike()
print(b1.name)
b1.helper()

