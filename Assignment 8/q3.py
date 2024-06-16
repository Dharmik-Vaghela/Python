import re
mystring=input("Enter String : ")
pattern="^[a-zA-Z]"
x=re.match(pattern,mystring)
print(x)