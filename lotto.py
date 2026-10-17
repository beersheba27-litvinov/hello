import random


def exists(numbers, num):
    """
    returns True if "num" exists in list "numbers" otherwise False
    """
    for n in numbers:
        if n == num:
            return True
    return False


def distinct_random_numbers(min, max, size):
    """

    returns list with "size" distinct random numbers
    each number >= "min" and <= "max"
    if creating "size" distinct random numbers is impossible, return empty array
    requirement: to use the above function "exists" and one while-loop
    """
    # TODO


print(distinct_random_numbers(1, 49, 7))
