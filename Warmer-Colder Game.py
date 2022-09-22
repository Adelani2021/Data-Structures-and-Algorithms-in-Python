Question 5 (Warmer/Colder Game)
import random
Choice = random.randrange (0, 100)
User = int(input("Enter your guessed number between 0 and 99 inclusive: "))
while User != Choice:
  if abs(Choice - User) > 50:
   print ("Cold")
   User = int(input("\nEnter your guessed number between 0 and 99 inclusive: "))
  for i in range (21, 51):
   if abs(Choice - User) == i:
    print ("Warmish")
    User = int(input("\nEnter your guessed number between 0 and 99 inclusive: "))
  for i in range (6, 21):
   if abs(Choice - User) == i:
    print ("Warm")
    User = int(input("\nEnter your guessed number between 0 and 99 inclusive: "))
  for i in range (1, 6):
   if abs(Choice - User) == i:
    print ("Hot!")
    User = int(input("\nEnter your guessed number between 0 and 99 inclusive: "))

print ("You win!")



  
