# #method returning multiple values
# class Cal:
#     def operation(self,a,b):
#         c1=a+b
#         c2=a-b
#         c3=a*b
#         c4=a/b
#         return c1,c2,c3,c4
# c=Cal()
# x=20
# y=10
# # res=c.operation(x,y)
# # print(res)
# r1,r2,r3,r4=c.operation(x,y)
# print(r1)
# print(r2)
# print(r3)
# print(r4)





# #method returning multiple values
# class Cal:
#     def operation(self,a,b):
#         c1=a+b
#         c2=a-b
#         c3=a*b
#         c4=a/b
#         return c1,c2,c3,c4

# c=Cal()
# x=20
# y=10
# # res=c.operation(x,y)
# # print(res)
# r1,r2,r3,r4=c.operation(x,y)
# print(r1)
# print(r2)
# print(r3)
# print(r4)

#whether str contains alphabetes numbers both alphabets and nos and some other characters
str=input("enter a string: ")
print(str)
if str.isaplha():
    print("str contains only alphabetes")
elif str.isdigits():
    print("str contains only numbers")
elif str.isalnum():
    print("str contains both alphabetes and numbers")
else:
    print("str contains some other characters")

