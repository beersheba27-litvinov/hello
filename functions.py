def intersection(l1: list[int], l2: list[int]) -> list[int]:
    """
    l1 - list containing non-repeated integer numbers
    l2 = list containing non-repeated integer numbers
    returns new list with integer numers existing in both input lists
    Examples: intersection([1, 2, 3], [4, 3, 1])=> [1, 3]
    intersection([1, 2, 3], [4, 5, 6])=> [];
    """
    return [num for num in l1 if (num in l2)]


def union(l1: list[int], l2: list[int]) -> list[int]:
    """
    l1 - list containing non-repeated integer numbers
    l2 = list containing non-repeated integer numbers
    returns new list with  integer numers existing  in ether list or both
    Result list shouldn't contain repeated numbers
    Examples: union([1, 2, 3], [4, 3, 1])=> [1, 2, 3, 4]
    union([1, 2, 3], [4, 5, 6])=> [1, 2, 3, 4, 5, 6]
    """
    for num in l2:
        if num not in l1:
            l1.append(num)
    return l1


def difference(l1: list[int], l2: list[int]) -> list[int]:
    """
    l1 - list containing non-repeated integer numbers
    l2 = list containing non-repeated integer numbers
    returns new list with  integer numers existing  in l1
    but non-existing  l2
    Examples: difference([1, 2, 3], [4, 3, 1])=> [2]
    difference([1, 2, 3], [4, 5, 6])=> [1, 2, 3]
    """
    return [num for num in l1 if (num not in l2)]


def _difference_with_accum(l1: list[int], l2: list[int], accum: list[int]) -> list[int]:
    """
    l1 - list containing non-repeated integer numbers
    l2 = list containing non-repeated integer numbers
    accum = accumulator containing integer numbers
    returns accumulator updated with integer numers existing in l1
    but non-existing  l2
    """
    for num in l1:
        if num not in l2:
            accum.append(num)
    return accum


def symmetric_difference(l1: list[int], l2: list[int]) -> list[int]:
    """
    l1 - list containing non-repeated integer numbers
    l2 = list containing non-repeated integer numbers
    returns new list with  integer numers existing  in either list but not in both
    Examples: symmetric_difference([1, 2, 3], [4, 3, 1])=> [2, 4]
    symmetric_difference([1, 2, 3], [4, 5, 6])=> [1, 2, 3, 4, 5, 6]
    """
    result: list[int] = _difference_with_accum(l1, l2, [])
    result = _difference_with_accum(l2, l1, result)
    return result


def remove_positive_greater_or_negative_less(
    numbers: list[int], positive_lim: int, negative_lim: int
) -> list[int]:
    """
    numbers - list with integer numbers
    returns new list containing all numbers from the input list
    except the positive ones greater than 'positive_lim' and the negative ones
    less than 'negative_lim'
    Example: remove_positive_greater_or_negative_less([1, 2, 11, -3, 10, 15], 10, -3)
    => [1, 2, -3, 10]
    """
    return [num for num in numbers if (negative_lim <= num <= positive_lim)]


def max_with_negative_duplicate(numbers: list[int]) -> int:
    """
    numbers - list with integer numbers
    returns the maximal element of "numbers" with existing negative duplicate
    (example of a number with negative duplicate: number 100, negative duplicate -100)
    If no such number exists, returns -1
    Examples: max_with_negative_duplicate([-100, 20, 10, -10, 1, 1, 5, -30, -20, 100]) => 100
    max_with_negative_duplicate([10, 20, -15, -11, 20]) => -1
    """
    result: int = -1
    for num in numbers:
        if num > result and (-num in numbers):
            result = num
    return result
