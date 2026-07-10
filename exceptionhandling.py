# a=int(input("enter a  no"))
# b=int(input("enter a no"))
# try:
#     c=a/b
#     print(c)
# except ZeroDivisionError:
#     print("ZeroDivisionError: division by zero")

# a=int(input("enter a no: "))
# b=int(input("enter a no: "))
# try:
#     c=a/b
#     print(c)
# except Exception as e:
#     print("error occurred")

#using functions how to hndle the error
def fun1():
    print("entering fun1")
    try:
        fun2()
    except Exception as e:
        print("error occurred in fun1")
    print("leaving fun1")
def fun2():
    print("entering fun2")
    res=10/0
    print(res) 
    print("leaving fun2")
print("program started")
fun1()
print("program ended")