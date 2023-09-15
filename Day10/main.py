import art
from replit import clear


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def continue_selection(text):
    selection = "None"
    while selection not in "yn":
        selection = input(text).lower()
    return selection


def calculator():
    clear()
    print(art.logo)
    num1 = float(input("Type the first number: "))
    should_continue = True
    while should_continue:
        operation = "None"
        while operation not in "+-*/":
            operation = input(f'Pick an operation ({" ".join(operations.keys())}): ')
        num2 = float(input("Type the next number: "))
        calc_function = operations[operation]
        calc_result = calc_function(num1, num2)
        decimals = 2
        print(f'{num1} {operation} {num2} = {calc_result:.{decimals}f}')
        selection = continue_selection(f'Do you wish to continue calculating with {calc_result}? Type "y" or "n"\n')
        if selection == "y":
            num1 = calc_result
        else:
            should_continue = False


end_of_program = False
while not end_of_program:
    calculator()
    calc_continue = continue_selection('Do you wish to use the calculator again? Type "y" or "n"\n')
    if calc_continue == "n":
        end_of_program = True
