bank=int(input("enter your amount:"))
if bank>0:
    print("amount is open")
    choice=int(input("enter your choice :"))
    print("enter1(for deposite)")
    print("enter2(for withdraw)")

    if choice==1:
        a=int(input("enter a amount for deposite:"))
        bank +=a
        print(f"this is new amount{bank}")
    elif choice==2:
        b=int(input("enter a amount for withdraw:"))
        bank -=b
        print(f"this is new {bank}")
    else:

        print("invalid number")

else:
    print("account is close")
    
    



