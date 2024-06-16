t1=("Python",1,2,3,"Java",'A','B')
print("Current Tuple : ",t1)

#print alternate values
for i in range(0,7):
    if i%2 == 0:
        print(t1[i])

#print value between index 1 to 5
print("Values between index 1 to 5 : ",t1[1:5])

#print the last value of tuple
print("Last value of tuple : ",t1[-1])