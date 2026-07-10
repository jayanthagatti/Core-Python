#encapsulation using setter and getter

class Book:
    def __init__(self,page):
        self.__pages=page
    def setter(self,val):
        if val>0:
            self.__pages=val
    def getter(self):
        return self.__pages
b1=Book(100)
res1=b1.getter()
print(res1)
b1.setter(200)
res2=b1.getter()
print(res2)

#normal encapsulation
class Person:
    def __init__(self):
        self.__pname=""
    def getter(self):
        return self.__pname
    def setter(self,val):
        self.__pname=val
p1=Person()
p1.setter("shreyas")
res1=p1.getter()
print(res1)

#property fucntion encapsulation
class Car:
    def __init__(self):
        self.__cname=""
    def setter(self,val):
        self.__cname=val
    def getter(self):
        return self.__cname
    getset=property(getter,setter)

c1=Car()
p1.getset="abc"
res=p1.getset
print(res)

#@property decorator
class car:
    def __init__(self):
        self.__cname=""
    @property
    def data(self):
        return self.__cname
    @data.setter
    def data(self,val):
        self.__cname=val

c=car()
c.data="audi"
res=c.data
print(res)
