import random   #imports the default Python random module, which allows for random number generation
import time     #imports the default Python time module, which allows for pauses in the program

counter    = 1    #defines the counter, which counts up to 10 each time a question is asked
score      = 0    #defines the user's score so it can be counted as they get questions right
numberOne  = 0    #opens the variable that stores the first number to be used in each question
numberTwo  = 0    #opens the variable that stores the second number to be used in each question
operator   = 0    #opens the variable that stores the number to be assigned to the operator in each question

name = input("What is your name user?  ")    #asks the user for their name so it can be used in the program.
whichClass = input("And which class are you in, 1, 2 or 3? ")

if whichClass == "1" or whichClass == "Class One":
   classOne = open("classOne.txt","a")
elif whichClass == "2" or whichClass == "Class Two":
   classTwo = open("classTwo.txt","a")
else:
   classThree = open("classThree.txt","a")

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

  if operator == 1:   #when the operator variable is 1, it runs the indented code
    print("Question",counter,"What is ",numberOne,"+",numberTwo,)    #prints the question using the add variable
    time.sleep(1)     #pauses the program for a second
    ans = add(numberOne, numberTwo)    #defines the question for the computer so it can be compared to the user's input
  elif operator == 2: #when the operator varialbe is 2, it runs the indented code
    print("Question",counter,"What is ",numberOne,"-",numberTwo,)    #prints the question using the subtract variable
    time.sleep(1)     #pauses the program for a second
    ans = subtract(numberOne, numberTwo) #defines the question for the computer so it can be compared to the user's input
  else:     #when the operator varialbe is 3, it runs the indented code
    print("Question",counter,"What is ",numberOne,"*",numberTwo)     #prints the question using the multiply variable
    time.sleep(1)     #pauses the program for a second
    ans = multiply(numberOne, numberTwo) #defines the question for the computer so it can be compared to the user's input

  res = int(input("Write your answer here: ")) #asks for the answer for the user so it can be checked to see if it is the right answer.

  if res == ans:      #when the result is the same as the answer, the indented code runs
    print("Congratulations,",name,"! 1 point scored.")   #prints a congratulations message to the user.
    time.sleep(1)     #pauses the program for a second
    score = score + 1 #adds one to the score variable
  else:    #when the result isn't the same as the answer, the indented code runs   
    print("Unlucky",name,"! No points scored.")    #prints an unluck message to the user
    time.sleep(1)     #pauses the program for a second

print("That's it! You've completed the quiz.\nYour total socore was...",score,"Well done,",name)   #concludes the program, printing the final score

time.sleep(1)
file.write("\n"name,":",score)
print("Your score has been saved to your class' file.")
time.sleep(1)

if score <= 5:    #when the score variable is less than or equal to 5, the indented code runs
  print("Do some practice and have another go.")   #prints an encouraging message to the user
elif score < 7:   #when the score variable is less than 7, the indented code runs
  print("You're almost there! have another try.")  #prints an 'almost there' message
else:    #when the score is more than 7, the score is more than 7, the  indented code runs
  print("You've done very well!")   #prints a congratulations message
