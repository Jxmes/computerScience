import random
import time
import sys

#variables
name = input("What's your name? ")
counter = 0
answer = ""
userscore = 0
begin = input("Are you ready? ")

time.sleep(1)

if begin == "yes":
    
    time.sleep(1)

    print("Welcome to the Maths Quiz",name,"!")

    time.sleep(1)
    
    while counter<10:
     number1 = random.randint(0,20)
     number2 = random.randint(0,15)
     operators = random.randint(1,3)

     if operators == 1:
        print("What is",number1,"+",number2,)
        ans = number1 + number2
        counter = counter+1

     elif operators == 2:
        print("What is",number1,"*",number2,)
        ans = number1 * number2
        counter = counter+1

     else:
        print("What is",number1,"-",number2,)
        ans = number1 - number2
        counter = counter+1

     useranswer = int(input()) 
     if useranswer == ans:
        print("Correct!")
        userscore = userscore + 1
     else:
        print("Wrong!")

    if userscore<5:
        time.sleep(1)
        print("Better luck next time",name,"you scored",userscore,"/ 10!")
    else:
        time.sleep(1)
        print("Congratulations",name,"you scored",userscore,"/ 10!")

else:
    print("James isn't worth oxygen!")
    sys.exit()

    time.sleep(4)








    
    
    








