from collections.abc import Callable, Sequence


def _move_max_to_end(
    items: list[object], length: int, key: Callable[[object], object] | None = None
) -> int:
    n_swaps: int = 0
    for i in range(length):
        item_current = items[i] if key is None else key(items[i])
        item_next = items[i + 1] if key is None else key(items[i + 1])
        if item_current > item_next:  # pyright: ignore[reportOperatorIssue]
            n_swaps += 1
            items[i], items[i + 1] = items[i + 1], items[i]
    return n_swaps


def bubble_sorted(
    items: Sequence[object], key: Callable[[object], object] | None = None
) -> list[object]:
    """
    Sequence[object] means immutable list, so items cannot be updated
    returns new list of objects sorted using algorithm "bubble sort"
      in accorgance with key function-converter like standard Python sorting
    items - sequence of any objects
    key - a function taking one object and returning converted object having standard operator ">"
          default value None designating standard Python sorting with no converting initial object
    For example, bubble_sort(numbers) - regular sort of numbers
                 bubble_sort(numbers, abs) - sort of numbers in accordance with their abs values
    Unlike the standard sorting methods of Python, the function may be called with no explicit specifying key=
    """
    sorted_items: list[object] = list(items)
    unsorted: bool = True
    size: int = len(sorted_items)
    while unsorted:
        size -= 1
        unsorted = bool(_move_max_to_end(sorted_items, size, key))
    return sorted_items


def even_asc_odd_desc(numbers: list[int]) -> list[int]:
    """
    returns new list of numbers sorted in the following order:
    The even numbers ordered by ascending order reside before odd numbers ordered by descending order
    For example, even_asc_odd_desc([-3, -10, 12, 3, -21, 6, 21, 5, 4 ]) returns [-10, 4, 6, 12, 21, 5, 3, -3, -21]
    """

    return bubble_sorted(
        numbers,
        lambda num: (0, num) if num % 2 == 0 else (1, -num),  # pyright: ignore[reportReturnType, reportUnknownLambdaType, reportOperatorIssue]
    )


def _binary_search(
    items: list[object], item: object, key: Callable[[object], object] | None = None
) -> int:
    left: int = 0
    right: int = len(items) - 1
    middle: int = (left + right) // 2
    item_comparable = item if key is None else key(item)

    while left <= right:
        items_middle = items[middle] if key is None else key(items[middle])

        if item_comparable > items_middle:  # pyright: ignore[reportOperatorIssue]
            left = middle + 1
        else:
            right = middle - 1
        middle = (left + right) // 2

    condition = (
        left < len(items)
        and (items[left] if key is None else key(items[left])) == item_comparable
    )
    return left if condition else -(left + 1)


def merge(
    part1: Sequence[object],
    part2: Sequence[object],
    key: Callable[[object], object] | None = None,
) -> list[object]:
    """
    part1 and part2 -  sorted in accordance with key function-converter lists of any objects
    key - a function taking one object and returning converted object having standard operator ">"
              default value None designating standard Python sorting with no converting initial objects
    returns new list, sorted in accordance with key function-converter, comprising of two lists-parts
    For example, merge([-11, 3, 5, 7], [-20, -10, 0, 4])  => [-20, -11, -10, 0, 3, 4, 5, 7]
    merge([3, 5, 7, -11 ], [ 0, 4, -10, -20 ], abs)  => [ 0, 3, 4, 5, 7, -10, -11,-20]
    """
    acceptor_list, donor_list = (
        (list(part1), list(part2))
        if len(part1) >= len(part2)
        else (list(part2), list(part1))
    )

    for obj in donor_list:
        index = _binary_search(acceptor_list, obj, key)
        index = index if index >= 0 else -(index + 1)
        acceptor_list[index:index] = [obj]

    return acceptor_list
