from collections.abc import Callable, Sequence
from typing import cast


def _merge[T, K](list1: list[T], list2: list[T], key: Callable[[T], T | K]) -> list[T]:
    i: int = 0
    j: int = 0
    len1 = len(list1)
    len2 = len(list2)
    result: list[T] = []

    while i < len1 and j < len2:
        if key(list1[i]) > key(list2[j]):  # pyright: ignore[reportOperatorIssue]
            result.append(list2[j])
            j += 1
        else:
            result.append(list1[i])
            i += 1

    result.extend(list1[i:])
    result.extend(list2[j:])

    return result


def _merge_pairs[T, K](
    sorted_sublists: list[list[T]], key: Callable[[T], T | K]
) -> list[list[T]]:
    merged_sublists = [
        _merge(sorted_sublists[i], sorted_sublists[i + 1], key)
        for i in range(0, len(sorted_sublists) - 1, 2)
    ]

    if len(sorted_sublists) % 2 == 1:
        merged_sublists.append(sorted_sublists[-1])

    return merged_sublists


def my_sorted[T, K](
    items: Sequence[T], /, *, key: Callable[[T], T | K] | None = None
) -> list[T]:
    """
    returns sorted by key list
    implementation according the following algorithm:
    1. Creating list of already sorted by key parts from "items"
      (no additional sorting is required)
    2. Merge of all parts from the created above list

    """
    result: list[T] = []

    if len(items) > 0:
        sorted_sublists: list[list[T]] = []

        if key is None:
            key = lambda item: item

        start = 0

        for i in range(1, len(items)):
            if key(items[i - 1]) > key(items[i]):  # pyright: ignore[reportOperatorIssue]
                sorted_sublists.append(cast(list[T], items[start:i]))
                start = i
        sorted_sublists.append(cast(list[T], items[start:]))

        while len(sorted_sublists) > 1:
            sorted_sublists = _merge_pairs(sorted_sublists, key)

        result = sorted_sublists[0]

    return result
