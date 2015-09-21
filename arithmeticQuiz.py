import random
import time

counter = 1
score = 0
numberOne = 0
numberTwo = 0
operatorList = [+,-,*]

for counter in range(0,10):
  numberOne = random.randint(0,11)
  numberTwo = random.randint(0,11)
  operator = random.choice(operatorList)
  print(numberOne, operator, numberTwo)
  
  question = numberOne, operator, numberTwo
  print(question)
  time.sleep(2)
  answer = eval(question)
  print(answer)
  
  #print (question, "=???")
  #reply = int(input("Enter your answer: "))
  #if reply == answer :]
  #  print ("Correct!")
  #else :
  #  print ("Unlucky!")
