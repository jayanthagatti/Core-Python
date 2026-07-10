class Student:
    def __init__(self,sname,sage,susn):
        self.name=sname
        self.age=sage
        self.usn=susn

# s1=Student("abc",22,76)
# s2=Student("xyz",25,78)
sname=input("enter student name: ")
sage=int(input("enter student age: "))
susn=input("enter student usn: ")

s1=Student(sname,sage,susn)
s2=Student(sname,sage,susn)
s3=Student(sname,sage,susn)
s4=Student(sname,sage,susn)
s5=Student(sname,sage,susn)

print("Name: ",s1.name)
print("Age: ",s1.age)
print("Usn: ",s1.usn)

print("Name: ",s2.name)
print("Age: ",s2.age)
print("Usn: ",s2.usn)

print("Name: ",s3.name)
print("Age: ",s3.age)
print("Usn: ",s3.usn)

print("Name: ",s4.name)
print("Age: ",s4.age)
print("Usn: ",s4.usn)

print("Name: ",s5.name)
print("Age: ",s5.age)
print("Usn: ",s5.usn)