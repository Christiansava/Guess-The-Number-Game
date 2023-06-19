#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Define number of attemps based on the difficulty.
def attempts(difficulty):
  """Define number of attemps based on the difficulty"""
  num_attempts = 0
  if difficulty == "hard":
    num_attempts = HARD_LEVEL_TURNS
  elif difficulty == "easy":
    num_attempts = EASY_LEVEL_TURNS

  return num_attempts

#Validate players guess against computer number
def validate_guess(computer_number, player_guess):
  """Validate players guess against computer number"""
  if player_guess == computer_number:
    return 2
  elif player_guess > computer_number:
    return 0
  else:
    return 1

#Return message based on guess
def result_message(guess_result, player_guess):
  """Return message based on guess"""
  if guess_result == 2:
    return f"You got it! The answer was {player_guess}."
  elif guess_result == 0:
    return "Too high."
  else:
    return "Too low."

#Main function that calls the other functions
def game():
  print(logo)
  
  print("Welcome to the Number Huessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  
  computer_number =random.randint(1, 100)
  
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  
  num_attempts = attempts(difficulty)
  
  finish_Game = False
  
  #Continue guessing while the number of guess is higher than 0
  while not finish_Game:
    print(f"You have {num_attempts} attempts remaining to guess the number.")
  
    player_guess = int(input("Make a guess: "))
  
    guess_result = validate_guess(computer_number, player_guess)
  
    print(result_message(guess_result, player_guess))
    
    if guess_result == 2:
      finish_Game = True
    elif guess_result != 2:
      num_attempts -= 1
      if num_attempts > 0:
        print("Guess again.")
      else:
        print("You've run out of guesses, you lose.")
        finish_Game = True

game()