num=int(input("Enter number of elements : "))
l1=[]
for i in range(0,num):
    a=input("Enter element : ")
    l1.insert(i,a)
for j in range(0,num):
    if j%2 == 0:
        print(l1[j])