#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
from random import *

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
computer_num = randint(0,100)

last_turn = 0
current_turn = 0
level = input("Choose a difficulty. Type 'easy' or 'hard': ")
if level == "easy":
    last_turn = 10
else:
    last_turn = 5

while current_turn != last_turn:
    user_num = int(input("Make a guess:"))
    current_turn += 1
    if user_num == computer_num:
        print(f"You got it! The answer was {computer_num}")
        current_turn = last_turn
    else:
        if user_num > computer_num:
            print("Too high.")
        else:
            print("Too low.")
        if current_turn == last_turn:
            print("You've run out of guesses, you lose.")
        else:
            print("Guess again.")
            print(f"You have  {last_turn - current_turn} attempts remaining to guess the number.")
