#pickling
# import pickle
# class Employee:
#     def __init__(self,name,age):
#         self.ename=name
#         self.eage=age
#     def disp(self):
#         print(self.ename)
#         print(self.eage)

# e=Employee("krishnajoshi",'55')
# e.disp()
# f=open("hi.txt","wb")
# pickle.dump(e,f)
# f.close()

#unpickling
import pickle
class Employee:
    def __init__(self,name,age):
        self.ename=name
        self.eage=age
    def disp(self):
        print(self.ename)
        print(self.eage)

f=open("hi.txt","rb")
e=pickle.load(f)
e.disp()
print("object is retrived")
f.close()