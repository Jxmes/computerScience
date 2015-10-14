#Name: James Hancock
#Candidate No. 6078
#Outwood Academy - 23148
#A453 Programming Task

import random #imports the default Python random module, which enables the user to generate random integers
import time #imports the default Python time module, which enables the user to add pauses in the program

#variables
name = input("What's your name? ") #asks the user for their name
counter = 0 #counts up so the program knows how many questions have been asked
answer = "" #asks for the answer so that the program can check if the answer is correct or incorrect
userscore = 0 #score counter so that the user knows how many questions they got right out of 10
begin = input("Are you ready? ") #asks if the user is ready to start the quiz

time.sleep(1) #creates a delay for 1 second

if begin == "yes": #if the user replies "yes" to the question, run the indented code

    time.sleep(1) #creates a delay for 1 second

    print("Welcome to the Maths Quiz",name,"!") #prints "Welcome to the Maths Quiz (name)?"

    time.sleep(1) #creates a delay for 1 second

    while counter<10: #while creates a loop
     number1 = random.randint(0,20) #randomly generates an integer between 0 and 20
     number2 = random.randint(0,15) #randomly generates an integer between 0 and 15
     operators = random.randint(1,3) #randomly generates one of the following operators, *,+, or -
    
     if operators == 1: #when the operator is equal to 1, run the indented code
        print("What is",number1,"+",number2,)
        ans = number1 + number2 #addition
        counter = counter+1 #adds 1 to the question counter

     elif operators == 2: #when the operator is equal to 2, run the indented code
        print("What is",number1,"*",number2,)
        ans = number1 * number2 #multiplication
        counter = counter+1 #adds 1 to the question counter

     else: #when the operator isn't 2 or 3, run the indented code
        print("What is",number1,"-",number2,)
        ans = number1 - number2 #subtraction
        counter = counter+1 #adds 1 to the question counter

     useranswer = int (input()) 
     if useranswer == ans: #if the answer is correct, run the indented code
        print("Correct!") #prints "Correct!" if the answer was correct
        userscore = userscore + 1 #adds 1 to the user's score
     else:
        print("Wrong!") #prints "Wrong!" if the answer was incorrect

    if userscore<5: #if the user's score is less than 5, run the indented code
        time.sleep(1) #creates a delay for 1 second
        print("Better luck next time",name,"you scored",userscore,"/ 10!") #prints "Better luck next time"(name)"you scored",(score), / 10!" if the score was less than 5
    else:
        time.sleep(1) #creates a delay for 1 second
        print("Congratulations",name,"you scored",userscore,"/ 10!") #prints "Congratulations"(name)"you scored",(score), / 10!" if the score was more than 5

else:
    print("Okay nevermind!") #prints "Okay nevermind!" if anything else other than "yes" is entered after, "Are you ready?"

time.sleep(4) #creates a 4 second delay before the program exits

