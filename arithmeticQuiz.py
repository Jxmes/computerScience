import random
import time

counter = 1
score = 0
numberOne = 0
numberTwo = 0
operator = 0

def add(x, y):
  return x + y;
  
def subtract (x, y):
  return x - y;
  
def multiply (x, y):
  return x * y;

for counter in range(0,11):
  numberOne = random.randint(0,11)
  numberTwo = random.randint(0,11)
  operator = random.randint(0,4)
  
  if operator == 1:
    ans = add(numberOne, numberTwo)
  elif operator == 2:
    ans = subtract(numberOne, numberTwo)
  else:
    ans = multiply(numberOne, numberTwo)
  
  print("Qestion ",counter,"What is ",ans)
  res = int(input("Write your answer here: "))
  
  if res == ans:
    print("Congratulations! 1 point scored.")
    score = score + 1
  else:
    print("Unlucky! No points scored.")
    
