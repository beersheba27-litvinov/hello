import functions

print(
    f"intersection([1, 2, 3], [4, 3, 1]), expected: [1, 3], actual: {functions.intersection([1, 2, 3], [4, 3, 1])}"
)
print(
    f"intersection([1, 2, 3], [4, 5, 6]), expected: [], actual: {functions.intersection([1, 2, 3], [4, 5, 6])}"
)

print(
    f"union([1, 2, 3], [4, 3, 1]), expected: [1, 2, 3, 4], actual: {functions.union([1, 2, 3], [4, 3, 1])}"
)
print(
    f"union([1, 2, 3], [4, 5, 6]), expected: [1, 2, 3, 4, 5, 6], actual: {functions.union([1, 2, 3], [4, 5, 6])}"
)

print(
    f"difference([1, 2, 3], [4, 3, 1]), expected: [2], actual: {functions.difference([1, 2, 3], [4, 3, 1])}"
)
print(
    f"difference([1, 2, 3], [4, 5, 6]), expected: [1, 2, 3], actual: {functions.difference([1, 2, 3], [4, 5, 6])}"
)

print(
    f"symmetric_difference([1, 2, 3], [4, 3, 1]), expected: [2, 4], actual: {functions.symmetric_difference([1, 2, 3], [4, 3, 1])}"
)
print(
    f"symmetric_difference([1, 2, 3], [4, 5, 6]), expected: [1, 2, 3, 4, 5, 6], actual: {functions.symmetric_difference([1, 2, 3], [4, 5, 6])}"
)

print(
    f"remove_positive_greater_or_negative_less([1, 2, 11, -3, 10, 15], 10, -3), expected: [2, 4], actual: {functions.remove_positive_greater_or_negative_less([1, 2, 11, -3, 10, 15], 10, -3)}"
)

print(
    f"max_with_negative_duplicate([-100, 20, 10, -10, 1, 1, 5, -30, -20, 100]), expected: 100, actual: {functions.max_with_negative_duplicate([-100, 20, 10, -10, 1, 1, 5, -30, -20, 100])}"
)
print(
    f"max_with_negative_duplicate(([10, 20, -15, -11, 20]), expected: -1, actual: {functions.max_with_negative_duplicate([10, 20, -15, -11, 20])}"
)
