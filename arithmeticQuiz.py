import random   #imports the default Python random module, which allows for random number generation
import time     #imports the default Python time module, which allows for pauses in the prgram

counter = 1     #defines the counter, which counts up to 10 each time a question is asked
score = 0       #defines the user's score so it can be counted as they get questions right
numberOne = 0   #opens the variable that stores the first number to be used in each question
numberTwo = 0   #opens the variable that stores the second number to be used in each question
operator = 0    #opens the variable that stores the number to be assigned to the operator in each question

name = input("What is your name user?  ")    #asks the user for their name so it can be used in the program.

while name == "":    #while the name variable is empty, it runs the code that is entered.
   time.sleep(1)     #pauses the program for a second
   name = input("Hello, \nWhat is your name? ")    #reasks for the user's name.

print("Weclome to the quiz,",name)     #welcomes the user to the quiz
time.sleep(1)   #pauses the program for a second

def add (x, y):  #defines the add variable
  return x + y;  #tells the computer what to do when the add variable is called

def subtract (x, y):  #defines the subtract variable
  return x - y;       #tells the computer what to do when the subtract variable is called

def multiply (x, y):  #defines the multiply variable
  return x * y;       #tells the computer what to do when the multiply variable is callled

for counter in range(0,10):        #when the counter variable is in the range of 1 to 10, it runs all the indented code
  counter = counter + 1            #adds one to the counter variable
  numberOne = random.randint(0,11) #randomly generates a number to be used in the question
  numberTwo = random.randint(0,11) #randomly generates a number to be used in the question
  operator = random.randint(1,3)   #randomly generates a number to be used in the question

  if operator == 1:
    print("Question",counter,"What is ",numberOne,"+",numberTwo,)
    time.sleep(1)
    ans = add(numberOne, numberTwo)
  elif operator == 2:
    print("Question",counter,"What is ",numberOne,"-",numberTwo,)
    time.sleep(1)
    ans = subtract(numberOne, numberTwo)
  else:
    print("Question",counter,"What is ",numberOne,"*",numberTwo)
    time.sleep(1)
    ans = multiply(numberOne, numberTwo)

  res = int(input("Write your answer here: "))

  if res == ans:
    print("Congratulations,",name,"! 1 point scored.")
    time.sleep(1)
    score = score + 1
  else:
    print("Unlucky",name,"! No points scored.")
    time.sleep(1)

print("That's it! You've completed the quiz.\nYour total socore was...",score,"Well done,",name)
if score <= 5:
  print("Do some practice and have another go.")
elif score < 7:
  print("You're almost there! have another try.")
else:
  print("You've done very well!")
