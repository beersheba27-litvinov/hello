import random
from collections.abc import Callable

from functions import get_all_not_in_range, get_all_range, my_sorted
from unittest_print import print_results, print_test

sorted_numbers = [1, 3, 5, 7, 9, 11]
provided_numbers = [-10, -3, 1, 20, 25, 30, 40, 41]
unsorted_numbers = [3, -2, -1, 0, 1, 2, -3]

get_all_range_tests: list[tuple[range | None, list[int]]] = [
    (range(3, 7), [3, 5]),
    (range(3, 8), [3, 5]),
    (range(4, 8), [5]),
    (range(-1, 20), [1, 3, 5, 7, 9, 11]),
    (range(1, 3), [1]),
    (range(11, 13), [11]),
    (range(-5, -1), []),
    (range(20, 30), []),
    (range(4, 5), []),
    (range(5, 5), []),
    (range(10, 5), []),
    (range(7, 3, -1), [5]),
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
    (range(1, 12, 4), [3, 7, 11]),
    (range(11, 0, -4), [1, 5, 9]),
]

my_sorted_tests: list[tuple[str, Callable[[int], int] | None, list[int]]] = [
    ("no key", None, [-3, -2, -1, 0, 1, 2, 3]),
    ("key=abs", abs, [0, -1, 1, -2, 2, 3, -3]),
    ("key=lambda num: num", lambda num: num, [-3, -2, -1, 0, 1, 2, 3]),
    ("key=lambda num: -num", lambda num: -num, [3, 2, 1, 0, -1, -2, -3]),
]

for allowed, expected in get_all_range_tests:
    print_test(
        f"get_all_range: {allowed} from {sorted_numbers}",
        expected,
        get_all_range(sorted_numbers, allowed),
    )
print_test(
    f"get_all_range: range(1, 41) from {provided_numbers}",
    [1, 20, 25, 30],
    get_all_range(provided_numbers, range(1, 41)),
)

for disallowed, expected in get_all_not_in_range_tests:
    print_test(
        f"get_all_not_in_range: {disallowed} from {sorted_numbers}",
        expected,
        get_all_not_in_range(sorted_numbers, disallowed),
    )
print_test(
    f"get_all_not_in_range: range(1, 41, 2) from {provided_numbers}",
    [-10, -3, 20, 30, 40, 41],
    get_all_not_in_range(provided_numbers, range(1, 41, 2)),
)

for description, key, expected in my_sorted_tests:
    print_test(
        f"my_sorted: {description} from {unsorted_numbers}",
        expected,
        my_sorted(unsorted_numbers, key=key),
    )

empty: list[int] = []
print_test("my_sorted: empty list", [], my_sorted(empty))
print_test("my_sorted: one item", [5], my_sorted([5]))
print_test(
    "my_sorted: input is untouched",
    [3, -2, -1, 0, 1, 2, -3],
    unsorted_numbers,
)

random_numbers = [random.randint(-1000, 1000) for _ in range(1000)]
print_test(
    "my_sorted: 1000 random numbers are not sorted before the call",
    False,
    random_numbers == sorted(random_numbers),
)
print_test(
    "my_sorted: 1000 random numbers, same as sorted",
    True,
    my_sorted(random_numbers) == sorted(random_numbers),
)
print_test(
    "my_sorted: 1000 random numbers, key=abs, same as sorted",
    True,
    my_sorted(random_numbers, key=abs) == sorted(random_numbers, key=abs),
)

print_results()
