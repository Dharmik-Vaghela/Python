num=int(input("Enter number of elements : "))
l1=[]
print("Current list : ",l1)
for i in range(0,num):
    a=input("Enter element : ")
    l1.insert(i,a)
print("Updated list : ",l1)