#text file
#create and write a file
# name=input("enter a name: ")
# ptr=open("hi.txt","w")
# ptr.write(name)
# ptr.close()

#read the file
# ptr1=open("hi.txt",'r')
# res=ptr1.read()
# print(res)
# ptr1.close()

#append the data or add some new data
# name=input("enter a name:")
# ptr=open("hi.txt","a")
# ptr.write(name)
# ptr.close()


# ptr1=open("hi.txt",'r')
# res=ptr1.readlines()
# print(res)
# ptr1.close()

# ptr=open('hi.txt','r')
# pos=ptr.tell()
# print(pos)
# res=ptr.read(7)
# print(res)
# pos1=ptr.tell()
# print(pos1)
# res1=ptr.seek(4)
# print(res1)
# pos2=ptr.tell()
# print(pos2)



#binary file
#reasd the binary file
ptr=open("car.jpeg",'rb')
data=ptr.read(5000)
print(data)
ptr.close()

#write the binary file
ptr1=open("newcar.jpeg",'wb')
ptr1.write(data)
ptr1.close()
