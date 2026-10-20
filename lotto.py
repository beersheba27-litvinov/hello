import random


def exists(numbers, num):
    """
    returns True if "num" exists in list "numbers" otherwise False
    """
    return len([x for x in numbers if x == num]) > 0


def distinct_random_numbers(min, max, size):
    """

    returns list with "size" distinct random numbers
    each number >= "min" and <= "max"
    if creating "size" distinct random numbers is impossible, return empty array
    requirement: to use the above function "exists" and one while-loop
    """
    numbers = []
    if max - min + 1 >= size:
        while len(numbers) < size:
            number = random.randint(min, max)
            if not exists(numbers, number):
                numbers.append(number)

    return numbers


print(distinct_random_numbers(1, 49, 7))
