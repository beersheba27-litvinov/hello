from collections.abc import Callable

from functions import get_all_not_in_range, get_all_range, my_sorted
from unittest_print import print_results, print_test

sorted_numbers = [1, 3, 5, 7, 9, 11]
unsorted_numbers = [3, -2, -1, 0, 1, 2, -3]

get_all_range_tests: list[tuple[range | None, list[int]]] = [
    (range(3, 7), [3, 5]),
    (range(4, 8), [5, 7]),
    (range(-1, 20), [1, 3, 5, 7, 9, 11]),
    (range(1, 2), [1]),
    (range(11, 12), [11]),
    (range(-5, -1), []),
    (range(20, 30), []),
    (range(4, 5), []),
    (range(5, 5), []),
    (range(10, 5), []),
    (range(7, 3, -1), [5, 7]),
    (None, [1, 3, 5, 7, 9, 11]),
]

get_all_not_in_range_tests: list[tuple[range, list[int]]] = [
    (range(3, 7), [1, 7, 9, 11]),
    (range(4, 8), [1, 3, 9, 11]),
    (range(-1, 20), []),
    (range(1, 2), [3, 5, 7, 9, 11]),
    (range(11, 12), [1, 3, 5, 7, 9]),
    (range(-5, -1), [1, 3, 5, 7, 9, 11]),
    (range(20, 30), [1, 3, 5, 7, 9, 11]),
    (range(4, 5), [1, 3, 5, 7, 9, 11]),
    (range(5, 5), [1, 3, 5, 7, 9, 11]),
    (range(10, 5), [1, 3, 5, 7, 9, 11]),
    (range(7, 3, -1), [1, 3, 9, 11]),
]


my_sorted_tests: list[tuple[Callable[[int], int] | None, list[int]]] = [
    (None, [-3, -2, -1, 0, 1, 2, 3]),
    (abs, [0, -1, 1, -2, 2, 3, -3]),
    (lambda num: num, [-3, -2, -1, 0, 1, 2, 3]),
    (lambda num: -num, [3, 2, 1, 0, -1, -2, -3]),
]

for allowed, expected in get_all_range_tests:
    print_test(
        f"get_all_range: {allowed} from {sorted_numbers}",
        expected,
        get_all_range(sorted_numbers, allowed),
    )

for disallowed, expected in get_all_not_in_range_tests:
    print_test(
        f"get_all_not_in_range: {disallowed} from {sorted_numbers}",
        expected,
        get_all_not_in_range(sorted_numbers, disallowed),
    )


for key, expected in my_sorted_tests:
    print_test(
        f"my_sorted: {key} from {unsorted_numbers}",
        expected,
        my_sorted(unsorted_numbers, key=key),
    )

print_results()
