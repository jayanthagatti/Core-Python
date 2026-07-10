class Calci:
    def __init__(self):
        self.brand="casio"
        self.cost=1700

    def add(self):
        a=10
        b=20
        c=a+b
        print(c)
c1=Calci()
print(c1.brand)
print(c1.cost)
c1.add()

class calci:
    def __init__(self):
        self.brand="casio"
        self.cost=1899

    def add(self):
        a=10
        b=20
        c=a+b
        return c
c2=calci()
print(c2.brand)
print(c2.cost)
res=c2.add()
print(res)


class calci:
    def __init__(self):
        self.brand="casio"
        self.cost=2865
    def add(self,a,b):
        c=a+b
        print(c)
c3=calci()
print(c3.brand)
print(c3.cost)
x=10
y=20
c3.add(x,y)

class calci:
    def __init__(self):
        self.brand="casio"
        self.cost=2552
    def add(self,a,b):
        c=a+b
        return c

c4=calci()
print(c4.brand)
print(c4.cost)
x=10
y=20
res=c4.add(x,y)
print(res)
