#using conditional statements
#take input from user
age=int(input("enter ur age:"))
if age>=18:
    print("Eligible to vote")
else:
    print("Not eligible")
#alternate way
if age >18:
    print("eligible")
elif age==18:
    print("eligible")
else:
    print("Not eligible")
#alternate way
#result= (age>=18) ? ("eligible"):"not eligible"
#print(result)
#alternate way
#(age>=18)? print("eligible"): print("Not eligible")

