try:
    a=int(input("Enter A : "))
    b=int(input("Enter B : "))
except ValueError:
    print("Error occurs")
else:
    sum=a+b
    print("Sum : ",sum)
finally:
    print("Program executed successfully")