#has a relationship program
# class Radio:
#     def turnOn(self,x):
#         if x==1:
#             print("radio is on")
#         else:
#             print("radio is off")
#
# class Car:
#     def __init__(self,min,max):
#         self.carmin=min
#         self.carmax=max
#         self.r=Radio()
# c1=Car(30,120)
# print(c1.carmin)
# print(c1.carmax)
# c1.r.turnOn(1)
# c1.r.turnOn(0)

#composed object

# class OS:
#     def __init__(self):
#         self.status=True
#         print("OS is ready")
#
#     def getOS(self):
#         print("OS is installing")
#
# class Mobile:
#     def __init__(self,name):
#         self.mname=name
#         self.o=OS()
#         print("mobile is ready")
#         print("with os installed")
#
# m1=Mobile("Samsung")
# print(m1.o.status)
# m1.o.getOS()
# print(m1.mname)
# del m1
# print(m1.o.status)


#aggregate

# class Charger:
#     def __init__(self,name):
#         self.cname=name
#
#     def getCharger(self):
#         print("mobile is charging")
#
# class Mobile:
#     def __init__(self,name):
#         self.cname=name
#         self.c=""
#
#     def hasMobile(self,P):
#         self.c=P
#
# m1=Mobile("Samsung")
# c1=Charger("Type C")
# m1.hasMobile(c1)
# print(m1.c.cname)
# m1.c.getCharger()
# del m1
# print(c1.cname)

#combination of composed and aggregate obj
class Brain:
    def __init__(self):
        self.status="Active"
        print("brain is working")
    def getBrain(self):
        print("human is having brain")


class Car:
    def __init__(self,name):
        self.cname=name
    def getCar(self):
        print("car is moving")

class Person:
    def __init__(self,name):
        self.pname=name
        self.b=Brain()
        self.c=""
    def hasCar(self,P):
        self.c=P

p1=Person("harshith")
c1=Car("audi")
print(p1.b.status)
p1.b.getBrain()
print(p1.pname)
p1.hasCar(c1)
print(p1.c.cname)
p1.c.getCar()
print(p1.pname)
del p1
# print(p1.b.status)
print(c1.cname)
p1.b.getBrain()

