# take 3 inputs from user and check which one is greater & it should check all the conditions

a=int(input("Entr Fisrst no:"))
b=int(input("Enter second no: "))
c=int(input("Enter third no:"))

if a>b and a>c:
    print("a is greater")
elif b>a and b>c:
    print("b is greater")
elif c>a and c>b:
    print("c is greater")
else:
    print("all are equal")