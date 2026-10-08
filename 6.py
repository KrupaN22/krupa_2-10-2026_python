a=40
b=70
c=int (input("enter your choice:"))
print("press 1 for addition")
print("press 2 for sub")
print("press 3 for mul")
print("press 4 for sup")

if c==1:
    print(f"addition for {a} + {b} = {a+b}")

elif c==2:
    print(f"sub for {a} - {b} = {a-b}")

elif c==3:
    print(f"mul for {a} * {b} = {a*b}")

elif c==4:
    print(f"sup for {a} / {b} = {a/b}")

else:
    print("hii")