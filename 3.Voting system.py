#using conditional statements
#take input from user
age=int(input("Enter ur age:"))
if age>=18:
    print(" You are Eligible to vote")
else:
    print("You are Not eligible")
#alternate way
if age >18:
    print("eligible")
elif age==18:
    print("Eligible")
else:
    print("Not eligible")
#alternate way
#result= (age>=18) ? ("eligible"):"not eligible"
#print(result)
#alternate way
#(age>=18)? print("eligible"): print("Not eligible")

