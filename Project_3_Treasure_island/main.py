from logo import LOGO
print(LOGO)
print("Welcome to the Treasure Island")
print("Your mission to find the treasure.")
choice1 = input("You'r at the crossroad, where do you want to go?, type 'left' or 'right'.\n").lower()

if choice1 == "left":
    choice2 = input("You've come to the lake, there is island in the middle of the lake, "
                    "type 'Wait' to wait for the boat, type 'Swim' to swim accross.\n").lower()
    if choice2 == "wait":
        choice3 = input("You arrived at the island unarmed, There is house with 3 door, "
                        "one yellow, one red and one blue, which color do you choose?\n").lower()
        if choice3 == "red":
            print("Burn by fire, Game over.")
        elif choice3 == "yellow":
            print("you win!")
        elif choice3 == "blue":
            print("Eaten by beast, Game over.")
        else:
            print("You have choose the door that does not exist, Game over")
    else:
        print("Attached by a oat, Game over.")
else:
    print("You fell into the hole, Game over.")