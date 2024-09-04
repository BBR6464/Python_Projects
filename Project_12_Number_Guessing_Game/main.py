import random
from art import logo
print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number = random.randint(1, 100)
difficulty = input(" Choose the difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
    attempts = 10
else:
    attempts = 5


while attempts > 0:
    print(f"you have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess == number:
         print(f"You got it! The answer was {number}.")
         break
    elif guess < guess:
        print("Too low.")
    else:
        print("Too high.")
    attempts -= 1

    if attempts == 0:
        print(f"You've run out of guesses, you loose. The answer was {number}")