# to take a random number, importing random 
import random
a=random.randint(1,100) # variable  a  stores some random value
flag=0 #to print try again statement if we can't guess the number in 10 chances
# imagine we have 10 chances to guess the random number
for i in range(10):
    n=int(input("Enter number:"))
    #we need give hints and help to find the number within 10 chances
    if n>a:
        print("Guess lower")
    elif n<a:
        print("guess higher")
    elif n==a:
        print("congratulations! you guessed correctly.")
        flag=1 
        #if we guesssed the correct number in 2 chance itself then no need of remaining chances,so break that loop
        break
if flag==0:
    print("sorry,chances are out of range , try again...")
