print("Welcome tp the Tip calculator")
bill = float(input("What's your total bill? \n$"))
tip = int(input("How much tip would you like to give" + " " + "23, 12 or 50 \n "))
people = int(input("How many people to split the bill? \n "))
tip_as_percentage = tip/100
tip_amount = tip_as_percentage * bill
total_bill = bill + tip_amount
bill_per_head = total_bill/people
final_bill = round(bill_per_head)
print(f"Each person should pay: ${final_bill} ")