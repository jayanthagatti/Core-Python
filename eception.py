# try:
#     a=int(input("enter a no: "))
#     b=int(input("enter a no: "))
#     res=a/b
#     print(res)
# except (ValueError,ZeroDivisionError) as e:
#     print("it is ve or zde")

# except Exception as e:
#     print("error occurred")


try:
    a=int(input("enter a no: "))
    b=int(input("enter a no: "))
    res=a/b
    print(res)

except Exception as e:
    print("error occurred")
    print(e)
