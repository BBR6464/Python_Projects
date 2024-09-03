import symbols
import random

print("What do you want to choose? type 0 for rock, 1 for paper and 2 for scissors")
user_choice = int(input())
computer_choice = random.randint(0,2)

if user_choice == 0:
    print(symbols.rock)

elif user_choice == 1:
    print(symbols.paper)

elif user_choice == 2:
    print(symbols.scissors)

else:
    print("Invalid chioce")

print("Computer choice: ")
if computer_choice == 0:
    print(symbols.rock)

elif computer_choice == 1:
    print(symbols.paper)

elif computer_choice == 2:
    print(symbols.scissors)


if user_choice == computer_choice:
    print("It's a draw")
elif user_choice == 0 and computer_choice == 1:
    print("You loose")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 1 and computer_choice == 0:
    print("you win!")
elif user_choice == 1 and computer_choice == 2:
    print("You loose")
elif user_choice == 2 and computer_choice == 0:
    print("You loose")
elif user_choice == 2 and computer_choice == 1:
    print("You win!")