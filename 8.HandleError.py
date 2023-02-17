"""Q8. Write a function that handles the ValueError exception that may be raised when trying to convert a string to
an integer. The function should prompt the user to enter a new string until a valid integer is entered. """


def handle_error(string):
    while True:
        try:
            number = int(string)
            break
        except ValueError:
            string = input("Invalid input. Please enter a valid number: ")
    return number


user_input = handle_error('abc')
print(user_input)
