#example for polymorphism with class
class Plane:
    def takeoff(self):
        print("plane is taking off")
    def fly(self):
        print("plane is flying")
class Passenger(Plane):
    def land(self):
        print("plane is landing")
class Cargo(Plane):
    def land(self):
        print("plane is landing")
class Fighter(Plane):
    def land(Self):
        print("plane is landing")
p1=Passenger()
c1=Cargo()
f1=Fighter()
def allowplane(ref):
    ref.takeoff()
    ref.fly()
    ref.land()
allowplane(p1)
allowplane(c1)
allowplane(f1)

#example for metod overriding
class A:
    def disp(self):
        print("inside class a")
class B(A):
    def disp(self):
        print("inside class b")

class C(B):
    def disp(self):
        print("inside class c")
c1=C()
c1.disp()
c1.disp()
c1.disp()

#method overloading
class A:
    def disp(self,a):
        print(a)
class B(A):
    def disp(self,a,b):
        print(a)
        print(b)
class C(B):
    def disp(self,a,b,c):
        print(a)
        print(b)
        print(c)
c1=C()
c1.disp(10,20,30)
c1.disp(10,20)
c1.disp(10)