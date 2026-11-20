from bisect import bisect_left, bisect_right
from collections.abc import Callable, Sequence
from math import sqrt


def get_all_range(numbers: Sequence[int], allowed: range | None = None) -> list[int]:
    """
    numbers - sorted list of numbers in ascending order
    allowed - range of numbers (may be empty)
    returns list of numbers that greater or equal minimal value of range and less than maximal value
    for empty range the function returns the empty list
    for missed second argument the function returns the same "numbers"
    """
    result: list[int] = []

    if allowed is None:
        result = list(numbers)
    elif len(allowed):
        start = bisect_left(numbers, min(allowed[0], allowed[-1]))
        end = bisect_right(numbers, max(allowed[0], allowed[-1]))
        result = list(numbers[start:end])
    return result


def get_all_not_in_range(numbers: Sequence[int], disallowed: range) -> list[int]:
    """
    numbers - sorted list of numbers in ascending order
    disallowed - range of numbers (may be empty)
     returns list of numbers from "numbers" that are not in a given range
    """

    result = list(numbers)
    if len(disallowed):
        start = bisect_left(numbers, min(disallowed[0], disallowed[-1]))
        end = bisect_right(numbers, max(disallowed[0], disallowed[-1]))
        del result[start:end]
    return result


def _move_max_to_end[T, K](items: list[T], size: int, key: Callable[[T], T | K]) -> int:
    n_swaps = 0
    for i in range(size):
        if key(items[i]) > key(items[i + 1]):  # pyright: ignore[reportOperatorIssue]
            items[i], items[i + 1] = items[i + 1], items[i]
            n_swaps += 1
    return n_swaps


def _bubble_sorted[T, K](
    items: Sequence[T], key: Callable[[T], T | K] | None = None
) -> list[T]:
    result = list(items)
    if key is None:
        key = lambda obj: obj
    size = len(result)
    unsorted = True
    while unsorted:
        size -= 1
        unsorted = _move_max_to_end(result, size, key) > 0
    return result


def _merge[T, K](
    part1: Sequence[T],
    part2: Sequence[T],
    key: Callable[[T], T | K] | None = None,
) -> list[T]:
    result: list[T] = []
    len1 = len(part1)
    len2 = len(part2)
    index1 = 0
    index2 = 0
    if key is None:
        key = lambda obj: obj
    while index1 < len1 and index2 < len2:
        if key(part1[index1]) > key(part2[index2]):  # pyright: ignore[reportOperatorIssue]
            result.append(part2[index2])
            index2 += 1
        else:
            result.append(part1[index1])
            index1 += 1
    result.extend(part1[index1:])
    result.extend(part2[index2:])
    return result


def my_sorted[T, K](
    items: Sequence[T], /, *, key: Callable[[T], T | K] | None = None
) -> list[T]:
    """
    returns sorted by key list
    implementation according the following algorithm:
    "items" is divided on the parts, each of which contains sqrt(len(items)) items
    Each part should be sorted separately by bubble sorting algorithm that you have already implemented
    After that all parts should be merged.
    No limitations for extra space
    Note: To use "sqrt" function from the module "math". This function returns float type
        so you should apply function "int" and the last part may contain more items
    """
    result: list[T] = []
    len_items = len(items)
    sqrt_items = int(sqrt(len(items)))
    start = 0

    # The last part may contain not more, but less elements (unlike the docstring).
    # If it matters, could you explain in the lecture -- why?
    while start < len_items:
        sublist = items[start : start + sqrt_items]
        result = _merge(result, _bubble_sorted(sublist, key), key)
        start += sqrt_items

    return result
