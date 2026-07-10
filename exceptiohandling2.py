# def fun1():
#     print("entering fun1")
#     try:
#         fun2()
#     except Exception as e:
#         print("error occurred in fun1")
#     print("leaving fun1")

# def fun2():
#     print("entering fun1")
#     try:
#         res=10/0
#         print(res)
#     except Exception as e:
#         print("error occurred in fun2")
#         raise e
#     print("leaving fun2")

# print("progra,m started")
# fun1()
# print("program ebnded")

def fun1():
    print("entering fun1")
    try:
        fun2()
    except Exception as e:
        print("error occurred in fun1")
    print("leaving fun1")

def fun2():
    print("entering fun1")
    try:
        res=10/0
        print(res)
    except Exception as e:
        print("error occurred in fun2")
        raise e
    finally:
        print("leaving fun2")

print("progra,m started")
fun1()
print("program ebnded")


#else block
a=int(input("enter a no: "))
b=int(input("enter a no: "))
try:
    res=a/b
    print(res)
except Exception as e:
    print("error occurred")
else:
    print("program runned successfully.....")