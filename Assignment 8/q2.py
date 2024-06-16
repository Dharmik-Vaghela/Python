import re
mystring=input("Enter a String : ")
pattern=r"^vaghela"
x=re.match(pattern,mystring)
print(x)