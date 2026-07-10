class Demo:
    def disp(self,a=10,b=20,c=30):
        print(a)
        print(b)
        print(c)

d1=Demo()
x=11
y=22
z=33
# d1.disp()
#d1.disp(x)
#d1.disp(x,y)
d1.disp(z)
d1.disp(c=z)
d1.disp(a=y,b=x,c=z)


