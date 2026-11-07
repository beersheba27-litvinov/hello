import functions

print(
    f"max_with_negative_duplicate([-100, 20, 10, -10, 1, 1, 5, -30, -20, 100]), expected: 100, actual: {functions.max_with_negative_duplicate([-100, 20, 10, -10, 1, 1, 5, -30, -20, 100])}"
)
print(
    f"max_with_negative_duplicate([10, 20, -15, -11, 20]), expected: -1, actual: {functions.max_with_negative_duplicate([10, 20, -15, -11, 20])}"
)

print(
    f"sumOfTwoExists([1, -1, 40, 50, 0], 0), expected: True, actual: {functions.sumOfTwoExists([1, -1, 40, 50, 0], 0)}"
)
print(
    f"sumOfTwoExists([1, -1, 40, 50, 0], 42), expected: False, actual: {functions.sumOfTwoExists([1, -1, 40, 50, 0], 42)}"
)
print(
    f"sumOfTwoExists([1, 10, 20], 2), expected: False, actual: {functions.sumOfTwoExists([1, 10, 20], 2)}"
)

numbers = [100, 90, 80, 70]
functions.bubble_sort(numbers)
print(f"bubble_sort([100, 90, 80, 70]), expected: [70, 80, 90, 100], actual: {numbers}")

print(
    f"remove_duplicates([-1, 0, 100, -1, 20, 80, 20]), expected: [-1, 0, 100,  20, 80], actual: {functions.remove_duplicates([-1, 0, 100, -1, 20, 80, 20])}"
)
