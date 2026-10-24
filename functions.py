def indexOf(numbers, num):
    """
    "numbers" - list with int numbers; "num" - int
    if "num" exists in "numbers", returns index of its first occurrence,
    otherwise -1. Examples: indexOf([10, 20, 30, 20, -1],20) => 1,
    indexOf([10, 20, 30, 20, -1],23) => -1
    """
    i = 0
    while i < len(numbers) and numbers[i] != num:
        i += 1
    return i if i < len(numbers) else -1


def lastIndexOf(numbers, num):
    """
    "numbers" - list with int numbers; "num" - int
    if "num" exists in "numbers", returns index of its last occurrence,
    otherwise -1. Examples: lastIndexOf([10, 20, 30, 20, -1],20) => 3,
    lastIndexOf([10, 20, 30, 20, -1],23) => -1
    """
    reversed_index = indexOf(numbers[::-1], num)
    return -1 if reversed_index == -1 else len(numbers) - reversed_index - 1


def min_even(numbers):
    """
    "numbers" - list with int numbers
    returns minimal even number
    assumption: at least one even number exists in "numbers"
    no need to check that assumption (usually the assumptions are never checked )
    example: min_even (-10001, 10, 20, 8, -7) => 8
    """
    even_numbers = [num for num in numbers if num % 2 == 0]
    result = even_numbers[0]
    for num in even_numbers:
        if num < result:
            result = num
    return result


def count(numbers, num):
    """
    "numbers" - list with int numbers; "num" - int
    returns count of "num" occurrences in "numbers".
      Examples: count([10, 20, 30, 20, -1],20) => 2,
    count([10, 20, 30, 20, -1],23) => 0
    """
    return len([x for x in numbers if x == num])


def sumOfTwoExists(numbers, sum):
    """
    Optional task for advanced students
    To apply only the types discussed at the course up to now
    "numbers" - list with int numbers; "sum" - int
    returns True if "numbers" includes two numbers, sum of which equals "sum"
    Examples: sumOfTwoExists([1, -1, 40, 50, 0], 0) => True;
    sumOfTwoExists([1, -1, 40, 50, 0], 42) => False
    """
    last_index = len(numbers) - 1
    i = 0
    while i < last_index and not (sum - numbers[i] in numbers[i + 1 : len(numbers)]):
        i += 1
    return i < last_index


print("indexOf", indexOf([10, 20, 30, 20, -1], 20))  # 1
print("indexOf", indexOf([10, 20, 30, 20, -1], 23))  # -1

print("lastIndexOf", lastIndexOf([10, 20, 30, 20, -1], 20))  # 3
print("lastIndexOf", lastIndexOf([10, 20, 30, 20, -1], 23))  # -1

print("min_even", min_even([-10001, 10, 20, 8, -7]))  # 8

print("count", count([10, 20, 30, 20, -1], 20))  # 2
print("count", count([10, 20, 30, 20, -1], 23))  # 0

print("sumOfTwoExists", sumOfTwoExists([1, -1, 40, 50, 0], 0))  #  True
print("sumOfTwoExists", sumOfTwoExists([1, -1, 40, 50, 0], 42))  #  False
