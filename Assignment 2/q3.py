per=int(input("Enter Percentage : "))

if per>=70:
	print("A Grade")
elif per>=65 and per<70:
	print("B+ Grade")
elif per>=60 and per<65:
	print("B Grade")
elif per>=55 and per<60:
	print("C Grade")
else:
	print("Fail")
