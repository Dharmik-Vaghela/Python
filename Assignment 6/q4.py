a=input("Enter A : ")
b=input("Enter B : ")

if a.isdigit() and b.isdigit():
    a=int(a)
    b=int(b)
    print("Sum : ",a+b)
else:
    print("Invalid Values")