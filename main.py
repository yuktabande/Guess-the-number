#ASCII art logo.
from art import logo
print(logo)
# Allow the player to submit a guess for a number between 1 and 100.
difficulty_level = input("choose a difficulty level. Type 'easy' or 'hard': ")
if difficulty_level == 'easy':
  turns = 10
else:
  turns = 5


import random
answer = random.randint(1,100)
#print(answer)
while turns != 0:
  guess = int(input("Enter a number between 1 to 100:"))
  if guess > answer:
    print("Too high")

  elif guess < answer:
    print("Too low")
# If they got the answer correct, show the actual answer to the player.
  elif guess == answer:
    print(f"You got it right! The answer is {answer}")
    break
# Track the number of turns remaining.
  turns -= 1
# If they run out of turns, provide feedback to the player. 
if turns == 0:
  print("oops! you ran out of turns")