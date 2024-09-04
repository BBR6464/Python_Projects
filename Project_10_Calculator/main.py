from clear import clear
from art import logo


def add(n1, n2):
    return n1 + n2


def substract(n1, n2):
    return n1 + n2


def multiply(n1, n2):
    return n1 * n2


def division(n1, n2):
    return n1/n2


operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": division
}


def calculator():
    print(logo)
    num1 = float(input("+"))
    for symbol in operations:
        print(symbol)


    should_continue = True


    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculator_function = operations[operation_symbol]
        answer = calculator_function(num1, num2)


        if input(f"Type 'y' to continue calculation with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            clear()
            calculator()


calculator()