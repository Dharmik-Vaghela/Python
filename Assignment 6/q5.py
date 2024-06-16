try:
    a=int(input("Enter A : "))
    b=int(input("Enter B : "))
    div=a/b
    print("Answer : ",div)
except ValueError:
    print("Please enter Integer Values")
except ZeroDivisionError:
    print("Devide by 0 is not possible")
except Exception as e:
    print("Error : ",e)
finally:
    print("Program executed successfully")