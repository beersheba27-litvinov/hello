from functions import get_all_not_in_range, get_all_range
from unittest_print import print_results, print_test

numbers = [1, 3, 5, 7, 9, 11]

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


for allowed, expected in get_all_range_tests:
    print_test(
        f"get_all_range: {allowed} from {numbers}",
        expected,
        get_all_range(numbers, allowed),
    )


print_results()
