import random
import time

def countdown(n):
	while(n > 0):
		time.sleep(0.5)
		print(n)
		
		n = n-1
		if n == 0:
			break

min = 1
max = 6

roll = "yes"

while (roll == "yes" or roll == "y"):
    print("Rolling the dice...")
    countdown(10)
    print("The value is",end = ' : ')
    print(random.randint(min, max))
   

    roll =input("Roll the dices again?")




