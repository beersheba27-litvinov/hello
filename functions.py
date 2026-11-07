def max_with_negative_duplicate(numbers: list[int]) -> int:
    """
    Algorithm complexity should be O[N]
    numbers - list with integer numbers
    returns the maximal element of "numbers" with existing negative duplicate
    (example of a number with negative duplicate: number 100, negative duplicate -100)
    If no such number exists, returns -1
    Examples: max_with_negative_duplicate([-100, 20, 10, -10, 1, 1, 5, -30, -20, 100]) => 100
    max_with_negative_duplicate([10, 20, -15, -11, 20]) => -1
    """
    result = -1
    set_numbers = set(numbers)
    for num in numbers:
        if num > 0 and -num in set_numbers and num > result:
            result = num
    return result


def sumOfTwoExists(numbers: list[int], sum: int) -> bool:
    """
    Algorithm complexity should be O[N]
    "numbers" - list with int numbers; "sum" - int
    returns True if "numbers" includes two numbers, sum of which equals "sum"
    Examples: sumOfTwoExists([1, -1, 40, 50, 0], 0) => True;
    sumOfTwoExists([1, -1, 40, 50, 0], 42) => False
    """
    set_numbers: set[int] = set()
    result = False
    length = len(numbers)
    index = 0
    while not result and index < length:
        if numbers[index] in set_numbers:
            result = True
        else:
            set_numbers.add(sum - numbers[index])
        index += 1
    return result


def move_max_to_end(numbers: list[int], iteration: int) -> bool:
    """
    "numbers" - list with int numbers
    moves the maximal number (that may occur in "numbers" several times) to the end of "numbers"
    returns True if the accepted list was already sorted
    """
    is_sorted = True
    for i in range(len(numbers) - 1 - iteration):
        if numbers[i] > numbers[i + 1]:
            is_sorted = False
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
    return is_sorted


def bubble_sort(numbers: list[int]) -> None:
    """
    Algorithm complexity is O[N^2]
    Write implementation of the bubble sorting algorithm
    Bubble sorting algorithm: sequentional pushing maximal numbers to the end
    Example: Initial list [100, 90, 80, 70] - worst case regarding total number of iterations
    1. Pushing 100 to the end of whole list, as a result there will be [90, 80, 70, 100] - 100 on its place at end
    2. Pushing 90 to the end of the part comprising of 3 ([90, 80, 70]) first elements, as a result there will be [ 80, 70, 90,100]
    3. Pushing 80 to the end of the part comprising of 2 ([80, 70]) first elements, as a result there will be [  70,80, 90,100]
    Totally 6 iterations: step 1 has 3 iterations, step 2 has 2 iterations ans step 4 has 1 iteratiion
    Common formula of the number of iterations for worst case is (n * (n - 1))/2
    """
    is_sorted = False
    index = 0
    length = len(numbers)
    while not is_sorted and index < length - 1:
        is_sorted = move_max_to_end(numbers, index)
        index += 1


def remove_duplicates(numbers: list[int]) -> list[int]:
    """
    Algorithm complexity O[N]
    returns new list containing all numbers from 'numbers' parameter
      except duplicates. The order should be kept
    Example:  'numbers' - [-1, 0, 100, -1, 20, 80, 20] the function should return
    new list [-1, 0, 100,  20, 80]
    """
    result: list[int] = []
    set_result: set[int] = set()
    for num in numbers:
        if num not in set_result:
            set_result.add(num)
            result.append(num)
    return result
