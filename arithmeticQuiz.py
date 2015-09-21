import random
import time

counter = 1
score = 0
numberOne = 0
numberTwo = 0
operator = 0

name = input("What is your name user?  ")
print("Weclome to the quiz,",name)
time.sleep(1)

def add(x, y):
  return x + y;
  
def subtract (x, y):
  return x - y;
  
def multiply (x, y):
  return x * y;

for counter in range(0,11):
  counter = counter + 1
  numberOne = random.randint(0,11)
  numberTwo = random.randint(0,11)
  operator = random.randint(0,4)
  
  if operator == 1:
    print("Question ",counter,"What is ",numberOne,"+",numberTwo,)
    ans = add(numberOne, numberTwo)
  elif operator == 2:
    print("Question ",counter,"What is ",numberOne,"-",numberTwo,)
    ans = subtract(numberOne, numberTwo)
  else:
    print("Question ",counter,"What is ",numberOne,"*",numberTwo)
    ans = multiply(numberOne, numberTwo)
  
  res = int(input("Write your answer here: "))
  
  if res == ans:
    print("Congratulations,",name,"! 1 point scored.")
    score = score + 1
  else:
    print("Unlucky",name,"! No points scored.")
  
print("That's it! You've completed the quiz.\nYour total socore was...",score,"Well done,",name)
