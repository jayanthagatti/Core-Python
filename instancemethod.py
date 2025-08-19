#no parameter no return value
class Calci:
    def __init__(self):
        self.brand="casio"
        self.price=1700
    def add(Self):
        a=10
        b=20
        c=a+b
        print(c)
c1=Calci()
print(c1.brand)
print(c1.price)
c1.add()

#no parameter with return value
class Calci:
    def __init__(self):
        self.brand="casio"
        self.price=1700
    def add(Self):
        a=10
        b=20
        c=a+b
        return c
c1=Calci()
print(c1.brand)
print(c1.price)
res=c1.add()
print(res)

#with parameter no return value
class Calci:
    def __init__(self):
        self.brand="casio"
        self.cost=1700
    def add(self,a,b):
        c=a+b
        print(c)

c1=Calci()
print(c1.brand)
print(c1.cost)
x=10
y=20
c1.add(x,y)

#with parameter with return value
class Calci:
    def __init__(self):
        self.brand="casio"
        self.cost=1700
    def add(self,a,b):
        c=a+b
        return c

c1=Calci()
print(c1.brand)
print(c1.cost)
x=10
y=20
res=c1.add(x,y)
print(res)