class A:
    def disp(self):
        print("inside A")

class B(A):
    def disp(self):
        print("inside B")

class C(B):
    def disp(self):
        print("inside C")

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
