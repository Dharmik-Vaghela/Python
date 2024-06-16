def sum(a):
    if a==1:
        return 1
    else:
        return a+sum(a-1)
    
num=int(input("Enter any number : "))
print(sum(num))