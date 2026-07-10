
class Student:
    def __init__(self):
        self.__name="jayanth"
        self.__age=20
        self.__marks=100
    def setname(self,name):
        if name!=0:
            self.__name=name
    def setage(self,age):
        if age!=0:
            self.__age=age
    def setmarks(self,marks):
        if marks!=0:
            self.__marks=marks
    def getname(self):
        print(self.__name)
    def getage(self):
        print(self.__age)
    def getmarks(self):
        print(self.__marks)
s=Student()
# s.setname("jayram")
# s.getname()
# s.setage(24)
# s.getage()
# s.setmarks(200)
# s.getmarks()
s.getname()
s.getage()
s.getmarks()