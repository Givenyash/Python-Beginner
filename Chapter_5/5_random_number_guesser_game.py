#Using a in-built library... 
#Random number guessing Game...

import random

num = random.randint(1,10)

count = 0

while True:
   guess = int(input("Please guess your number between 1 and 10 :"))

   if num == guess:
       count += 1
       print(f"You guessed the correct number in {count} tries.")
       break

   elif num < guess:
       count += 1
       print("Go a little lower")

   elif num > guess:
       count += 1
       print("Go a little higher")

   else:
       count += 1
       print("Sorry you are wrong")