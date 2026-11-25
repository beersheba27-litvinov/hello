from collections.abc import Callable
from random import randint

from functions import my_sorted
from unittest_print import print_results, print_test

numbers: list[int] = [-10, -3, 1, 20, 25, 30, 40, 41]
N_ITEMS = 1023
unsorted_numbers: list[int] = [randint(1, 100000) for _ in range(N_ITEMS)]
sorted_numbers_by_str: list[int] = my_sorted(unsorted_numbers, key=lambda a: str(a))
sorted_numbers: list[int] = my_sorted(unsorted_numbers)
test_numbers = [20, -10, 1, 30, -11, 1, -50]
test_numbers_sorted = my_sorted(test_numbers)


def is_sorted[T, K](lst: list[T], key: Callable[[T], T | K] | None = None) -> bool:
    lim = len(lst) - 1
    i = 0
    if key is None:
        key = lambda a: a
    while i < lim and key(lst[i]) <= key(lst[i + 1]):  # type: ignore
        i += 1
    return i >= lim


print_test(f"sorting list {test_numbers}", sorted(test_numbers), test_numbers_sorted)
print_test(
    f"sorting list with {N_ITEMS} random numbers by key converter to strings",
    True,
    is_sorted(sorted_numbers_by_str, key=lambda a: str(a)),
)
print_test(
    f"sorting list with {N_ITEMS} random numbers ", True, is_sorted(sorted_numbers)
)

print_results()
