import re
mystring=input("Enter a String : ")
pattern=r"^[a-zA-Z0-9]+$"

if re.match(pattern,mystring):
    print("It contains only given characters")
else:
    print("It contains other than given characters")