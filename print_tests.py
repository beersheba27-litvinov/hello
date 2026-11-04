import functions

print(
    f"min_max_average([1, 2, 3, 4, 5, 6]), expected: (1, 6, 3.5), actual: {functions.min_max_average([1, 2, 3, 4, 5, 6])}"
)

numbers = [100, 20, 30, 40, 50]
functions.move_max_to_end(numbers)
print(f"numbers, expected: [20, 30, 40, 50, 100], actual: {numbers}")

numbers = [100, 100, 20, 30, 40, 50]
functions.move_max_to_end(numbers)
print(f"numbers, expected: [100, 20, 30, 40, 50, 100], actual: {numbers}")
