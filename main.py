#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from random import randint
from ark import logo

random_number = randint(1,100)
print(logo)

print("Welcome to the Number Guessing Game! \nI'm thinking of number between 1 and 100 \nTry to guess the number")
# print(f"test_phase: {random_number}")
difficulty_level = input("Choose a difficulty.Type 'easy' or 'hard':  ").lower()

if difficulty_level == "easy":
    lives = 10
elif difficulty_level == "hard":
    lives = 5
else:
    print("Invalid Entry")
    lives = 0



while lives > 0:
    print(f"You have {lives} attempts remaining to guess the number")
    guess_number = int(input("Make a guess: "))
    if guess_number > 100 or guess_number < 0:
        print("Please enter a number in the range 1 and 100 ")
    elif guess_number == random_number:
        print(f"You got it! The answer was {random_number}")
        lives = 0
    elif guess_number < random_number:
        print("Too low")
    else:
        print("Too high")
    lives -=1
    if lives == 0:
        print("You've run out of guesses,you loss")