# date: 14/09/15
# username: A1fus
# name: Alfie Bowman
# description: Python gneral knowledge quiz

import time    #imports the time module which allows for a pause inbetween printing

score = 0    #defines the user's score before starting

name = input("What is your name user?   ")

print("Welcome to The Quiz, ",name,"\nWe'll be asking a series of general knowledge questions.")    #introduces the user to the quiz on two seperate lines
time.sleep(1)    #stops the program for one second

answerOne = input("Question 1:\nWhich US state is named on the label of a Jack Daniels bottle?   ")
time.sleep(1)
if answerOne == "Tennessee":
    print("Correct! You scored a point (☞ﾟヮﾟ)☞")
    time.sleep(1)
    score = score + 1
else:
    print("Unlucky! No points scored ಠ_ಠ.")
    time.sleep(1)

answerTwo = input("Question 2:\nA phlebotomist extracts what from the human body?   ")
time.sleep(1)
if answerTwo == "blood":
     print("Correct! You scored a point (☞ﾟヮﾟ)☞")
     time.sleep(1)
     score = score + 1
else:
    print("Unlucky! No points scored ಠ_ಠ.")
    time.sleep(1)

answerThree = input("Question 3:\nWhich planet is closest to the sun?   ")
time.sleep(1)
if answerThree == "Mercury":
     print("Correct! You scored a point (☞ﾟヮﾟ)☞")
     time.sleep(1)
     score = score + 1
else:
    print("Unlucky! No points scored ಠ_ಠ.")
    time.sleep(1)

answerFour = input("Question4:\nIn a VAT tribunal in 1991, were Jaffa Cakes ruled to be a cake or a biscuit?    ")
time.sleep(1)
if answerFour == "cake":
     print("Correct! You scored a point (☞ﾟヮﾟ)☞")
     time.sleep(1)
     score = score + 1
else:
    print("Unlucky! No points scored ಠ_ಠ.")
    time.sleep(1) #this makes it sleep

answerFive = input("Question 5:\nSince 1995, how many teams compete in The Rugby World Cup?    ")
time.sleep(1)
if answerFour == "20"0:
     print("Correct! You scored a point (☞ﾟヮﾟ)☞")
     time.sleep(1)
     score = score + 1
else:
    print("Unlucky! No points scored ಠ_ಠ.")
    time.sleep(1)

print("And that's it! your total score was...,")
time.sleep(2)
print(score,"!!!\nCONGRATULATIONS (づ｡◕‿‿◕｡)づ")
print(name)
