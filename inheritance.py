# class Parent:
#     def __init__(self):
#         self.a=10
# class Child(Parent):
#     def __init__(self):
#         Parent.__init__(self)
#         self.b=20
# c1=Child()
# print(c1.b)
# print(c1.a)
#
# class A:
#     def __init__(self):
#         self.a=10
#
# class B(A):
#     def __init__(self):
#         A.__init__(self)
#         self.b=20
#
# class C(B):
#     def __init__(self):
#         B.__init__(self)
#         self.c=30
# c1=C()
# print(c1.c)
# print(c1.b)
# print(c1.a)

# class A:
#     def __init__(self):
#         self.a=10
#
# class B(A):
#     def __init__(self):
#        super().__init__()
#         self.b=20
#
# class C(B):
#     def __init__(self):
#         super().__init__()
#         self.c=30
# c1=C()
# print(c1.c)
# print(c1.b)
# print(c1.a)


# class Plane:
#     def takeoff(self):
#         print("plane has been takeoff")
#     def fly(self):
#         print("plane is flying")
#     def land(self):
#         print("plane has been landed")
#
# class Passenger(Plane):
#     def carry_p(self):
#         print("plane carries passengers")
#
# class Cargo(Plane):
#     def carry_g(self):
#         print("plane carries goods")
#
# class Fighter(Plane):
#     def carry_w(self):
#         print("plane carries weapons")
#
# p1=Passenger()
# c1=Cargo()
# f1=Fighter()
# p1.takeoff()
# p1.fly()
# p1.land()
# p1.carry_p()
# c1.takeoff()
# c1.fly()
# c1.land()
# c1.carry_g()
# f1.takeoff()
# f1.fly()
# f1.land()
# f1.carry_w()


class Animal:
    def eat(self):
        print("animal is eating")
    def sleep(self):
        print("animal is sleeping")
    def hunt(self):
        print("animal is hunting")

class Tiger(Animal):
    pass
class Hyena(Animal):
    pass
class Monkey(Animal):
    pass
t1=Tiger()
h1=Hyena()
m1=Monkey()
t1.eat()
t1.sleep()
t1.hunt()
h1.eat()
h1.sleep()
h1.hunt()
m1.eat()
m1.sleep()
m1.hunt()