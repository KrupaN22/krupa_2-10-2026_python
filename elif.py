
maths = int(input("enter your marks for maths:"))


guj = int(input("enter your marks for guj:"))


hindi = int(input("enter your marks for hindi:"))


english = int(input("enter your marks for english:"))


total= hindi+english+maths+guj
print(total)
pr=total/4
print(pr)

if pr >=90:
    print("student is A grade")

elif pr >=80:
    print("student is B grade")

elif pr >=70:
    print("student is C grade")

elif pr >=50:
    print("student is D grade")

elif pr >=30:
    print("failed")








