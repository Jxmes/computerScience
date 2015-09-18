import random
import time

counter = 1
score = 0
numberOne = 0
numberTwo = 0
operator = 0

while counter < 10:
  numberOne = random.randint(0,11)
  numberTwo = random.randint(0,11)
  operator = random.randint(0,4)
  
  if operator == 1:
    operator = +
  elif operator == 2:
    operator = -
  else:
    operator = *
  
  answer = int(input("Question ",counter,numberOne,operator,numberTwo))
