"""Q7. Write a function that takes a list of numbers and returns the sum of the numbers that are divisible by 3 or 5.
The function should use a generator expression to accomplish this. """


def divisible_by_3_or_5(numbers):
    return sum(number for number in numbers if number % 3 == 0 or number % 5 == 0)


print(divisible_by_3_or_5([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
