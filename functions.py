from bisect import bisect_left
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
        end = bisect_left(numbers, max(allowed[0], allowed[-1]))
        result = [numbers[i] for i in range(start, end)]
    return result


def get_all_not_in_range(numbers: Sequence[int], disallowed: range) -> list[int]:
    """
    numbers - sorted list of numbers in ascending order
    disallowed - range of numbers (may be empty)
     returns list of numbers from "numbers" that are not in a given range
    """

    return [num for num in numbers if num not in disallowed]


def _move_max_to_end[T, K](items: list[T], size: int, key: Callable[[T], T | K]) -> int:
    n_swaps = 0
    for i in range(size):
        if key(items[i]) > key(items[i + 1]):  # pyright: ignore[reportOperatorIssue]
            items[i], items[i + 1] = items[i + 1], items[i]
            n_swaps += 1
    return n_swaps


def _bubble_sort[T, K](items: list[T], key: Callable[[T], T | K]) -> None:
    size = len(items)
    unsorted = True
    while unsorted:
        size -= 1
        unsorted = _move_max_to_end(items, size, key) > 0


def _merge[T, K](
    part1: Sequence[T],
    part2: Sequence[T],
    key: Callable[[T], T | K],
) -> list[T]:
    result: list[T] = []
    len1 = len(part1)
    len2 = len(part2)
    index1 = 0
    index2 = 0

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
    sqrt_items = int(sqrt(len_items))
    start = 0
    key = key if key is not None else lambda obj: obj

    # The last part may contain not more, but less elements (unlike the docstring).
    # If it matters, could you explain in the lecture -- why?
    while start < len_items:
        stop = min(start + sqrt_items, len_items)
        sublist = [items[i] for i in range(start, stop)]
        _bubble_sort(sublist, key)
        result = _merge(result, sublist, key)
        start += sqrt_items

    return result
