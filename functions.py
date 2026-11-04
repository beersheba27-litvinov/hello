def min_max_average(numbers: list[int]) -> tuple[int, int, float]:
    """
    "numbers" - list with int numbers
    returns tuple of minimal number, maximal number and average (float)
    assumption: "numbers" is not empty
    """

    min_num = numbers[0]
    max_num = min_num
    total = 0
    for num in numbers:
        total += num
        if num > max_num:
            max_num = num
        elif num < min_num:
            min_num = num
    return min_num, max_num, total / len(numbers)


def move_max_to_end(numbers: list[int]):
    """
    "numbers" - list with int numbers
    moves the maximal number (that may occur in "numbers" several times) to the end of "numbers"
    returns nothing
    """
    max_index = 0
    for i, num in enumerate(numbers):
        if num > numbers[max_index]:
            max_index = i
    max_num = numbers[max_index]

    for i in range(max_index, len(numbers) - 1):
        numbers[i] = numbers[i + 1]
    numbers[len(numbers) - 1] = max_num
