from bisect import bisect_left, bisect_right
from collections.abc import Callable, Sequence


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


def get_all_not_in_range(
    numbers: Sequence[int], disallowed: range | None = None
) -> list[int]:
    """
    numbers - sorted list of numbers in ascending order
    disallowed - range of numbers (may be empty)
     returns list of numbers from "numbers" that are not in a given range
    """


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
