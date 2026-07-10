#single threading
import time
class Demo:
    def prtname(self):
        l=["xyz","abc","abhi"]
        for i in l:
            print(i)
            time.sleep(3)
    def prtnum(self):
        for i in range(10):
            print(i)
            time.sleep(2)
    def add(self):
        a=10
        b=20
        c=a+b
        print(c)
d1=Demo()
d1.prtname()
d1.prtnum()
d1.add()