import time

laughCounter = 0
while 0 < 1:
  laughYes = input("Has bowman laughed in the last 10 seconds?  ")
  if laughYes == "yes":
    laughCounter = laughCounter + 1
    print("Bowman laughed once.\n Bowman has laughed",laughCounter,"times.")
