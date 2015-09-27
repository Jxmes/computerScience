import random
import time

counter = 1
score = 0
numberOne = 0
numberTwo = 0
operator = 0

name = input("What is your name user?  ")

while name == "":
   time.sleep(1)
   name = input("Hello, \nWhat is your name? ")

print("Weclome to the quiz,",name)
time.sleep(1)

def add(x, y):
  return x + y;

def subtract (x, y):
  return x - y;

def multiply (x, y):
  return x * y;

for counter in range(0,10):
  counter = counter + 1
  numberOne = random.randint(0,11)
  numberTwo = random.randint(0,11)
  operator = random.randint(1,3)

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
