import re
mystring="My name is Dharmik Vaghela"
print("String before replacement : ",mystring)
rep="Khushi"
x=re.sub("Dharmik",rep,mystring)
print("String after Replacement  : ",x)