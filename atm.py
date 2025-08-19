import time
password=1234
Balance=40000
print("Welcome to SBI ATM Bank")
print("insert your card")
card=int(input("Press 1.Yes\n 2.No"))
if card==1:
    print("Select the Language")
    print("Press 1.English\n 2.Kannada\n 3.telugu")
    lang=int(input())
    if lang==1:
        print("print enter your pin")
        pin=int(input())
        if pin==password:
            print("select  the option")
            print("1.Balance Enq 2.withdrawl")
            opt=int(input())
            if opt==1:
                print("your available balance is",Balance)
            elif opt==2:
                print("enter the amount")
                amt=int(input())
                if amt<Balance and amt%100==0:
                    print("no balance")
                print("your transaction is processing")
                time.sleep(4)
                print("Please collect your cash")
                time.sleep(3)
                print("do you want to check your balance")
                print("1.yes 2.no")
                choice=int(input())
                if choice==1:
                    print("your available balance is",Balance-amt) 
                    print("thank you visit again")
                else:
                    print("thank you visit again")
            else:
                print("wrong option")


        else:
            print("wrong pin")



    else:
        print("Please select only english")


else:
    print("insert the card properly")


