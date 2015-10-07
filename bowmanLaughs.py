##################################
#Created for James Hancock
#By Alfie 'A1fus' Bowman
#On the 7th of October 2015
##################################


import time

laughCounter = 0
while 0 < 1:
  laughYes = input("Has bowman laughed in the last 10 seconds?  ")
  
  if laughYes == "yes":
    laughCounter = laughCounter + 1
    print("Bowman laughed.\n Bowman has laughed",laughCounter,"times since the counter started.")
  else:
    print("Congratulations Bowman, you have completed the impossible.")
  
  time.sleep(10)
