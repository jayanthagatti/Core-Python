# def add():
#     a=1
#     b=2
#     c=a+b
#     print(c)
# add()

#types of functions
#1
# def add():
#     a=10
#     b=20
#     c=a+b
#     print(c)
# add()

# #2
# def add():
#     a=10
#     b=20
#     c=a+b
#     return c
# res=add()
# print(res)

# #3
# def add(a,b):
#     c=a+b
#     print(c)
# x=10
# y=20
# add(x,y)

# #4
# def add(a,b):
#     c=a+b
#     return c
# x=10
# y=20
# print(add(x,y))

#invoke the fn through var
# def fun1():
#     print("inside fun1")
# def fun2():
#     print("inside fun2")

# print(fun1)
# print(fun2)
# ptr1=fun1
# ptr2=fun2
# ptr1()
# ptr2()


# def fun1():
#     print("inside fun1")
# def fun2(ref):
#     print("entering fun2")
#     ref()
#     print("leaving fun2")
# fun1()
# fun2(fun1)