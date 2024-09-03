import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the Pypassword generator!")
nr_latter = int(input("How many letters would you like in your password? "))
nr_number = int(input("How many number would you like? "))
nr_symbol = int(input("How many number would you like? "))

password_list = []

for latter in range(0, nr_latter):
    latter = random.choice(letters)
    password_list.append(latter)

for num in range(0, nr_number):
    num = random.choice(numbers)
    password_list.append(num)

for sym in range(0, nr_symbol):
    sym = random.choice(symbols)
    password_list.append(sym)

random.shuffle(password_list)
password = " "

for char in password_list:
    password += char

print(f"Your password is : {password}")