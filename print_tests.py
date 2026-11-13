import functions
import unittest_print

numbers = [-2, -10, 12, 3, -22, 6, 21, 5, 4]
sorted_numbers = [-22, -10, -2, 3, 4, 5, 6, 12, 21]
sorted_numbers_abs = [-2, 3, 4, 5, 6, -10, 12, 21, -22]
sorted_even_odd = [-22, -10, -2, 4, 6, 12, 21, 5, 3]
strings = ["lmn", "aaaaaaa", "w", "bb", "B", "cc"]
sorted_len_str = ["B", "w", "bb", "cc", "lmn", "aaaaaaa"]
sorted_strings = ["B", "aaaaaaa", "bb", "cc", "lmn", "w"]
part1 = [3, 5, 7, -11]
part2 = [0, 4, -10, -20]
part2_with_duplicate = [3, 4, -10, -20]
merge_expected = [0, 3, 4, 5, 7, -10, -11, -20]
merge_with_duplicate_expected = [3, 3, 4, 5, 7, -10, -11, -20]
part1_standard = [1, 2, 3, 4]
part2_standard = [1, 3, 5, 6]
merge_standard_expected = [1, 1, 2, 3, 3, 4, 5, 6]

unittest_print.print_test(
    f"Sort of list {numbers}", sorted_numbers, functions.bubble_sorted(numbers)
)
unittest_print.print_test(
    f"Sort of list {numbers} according to abs values",
    sorted_numbers_abs,
    functions.bubble_sorted(numbers, abs),  # pyright: ignore[reportArgumentType]
)

unittest_print.print_test(
    f"Sort of list {strings} ",
    sorted_len_str,
    functions.bubble_sorted(strings, lambda s: (len(str(s)), s)),
)

unittest_print.print_test(
    f"Sort of list {numbers} according to even first in Asc, odd after even in Desc",
    sorted_even_odd,
    functions.even_asc_odd_desc(numbers),
)

unittest_print.print_test(
    "Initial sequence is untouched",
    [-2, -10, 12, 3, -22, 6, 21, 5, 4],
    numbers,
)

unittest_print.print_test(
    f"merge of two parts {part1} and {part2} according to abs values",
    merge_expected,
    functions.merge(part1, part2, abs),  # pyright: ignore[reportArgumentType]
)
unittest_print.print_test(
    f"merge of two parts {part1} and {part2_with_duplicate} (with duplicate) according to abs values",
    merge_with_duplicate_expected,
    functions.merge(part1, part2_with_duplicate, abs),  # pyright: ignore[reportArgumentType]
)
unittest_print.print_test(
    f"merge of two parts {part1_standard} and {part2_standard} according to standard comparing",
    merge_standard_expected,
    functions.merge(part1_standard, part2_standard),
)

unittest_print.print_results()
