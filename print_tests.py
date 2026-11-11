import functions

numbers: list[int] = [10, 10, 10, 20, 20, 20, 30, 30, 40]
numbers_ins7 = numbers.copy()
numbers_ins19 = numbers.copy()
numbers_ins20 = numbers.copy()
numbers_ins45 = numbers.copy()
functions.insert_sorted(numbers_ins7, 7)
functions.insert_sorted(numbers_ins19, 19)
functions.insert_sorted(numbers_ins20, 20)
functions.insert_sorted(numbers_ins45, 45)
print(
    f"list is {numbers}, index of 10 is expected - 0, actual -\
 {functions.binary_search(numbers, 10)}"
)
print(
    f"list is {numbers}, index of 20 is expected - 3, actual -\
 {functions.binary_search(numbers, 20)}"
)
print(
    f"list is {numbers}, index of 40 is expected - 8, actual -\
 {functions.binary_search(numbers, 40)}"
)
print(
    f"list is {numbers}, index of 5 is expected - -1, actual -\
 {functions.binary_search(numbers, 5)}"
)
print(
    f"list is {numbers}, index of 15 is expected - -4, actual -\
 {functions.binary_search(numbers, 15)}"
)
print(
    f"list is {numbers}, index of 50 is expected - -10, actual -\
 {functions.binary_search(numbers, 50)}"
)

print(
    f"initial array is {numbers}, after iserting 7 the expected list is\
[7, 10, 10, 10, 20, 20, 20, 30, 30, 40],the actual is {numbers_ins7}"
)
print(
    f"initial array is {numbers}, after iserting 19 the expected list is\
[ 10, 10, 10, 19, 20, 20, 20, 30, 30, 40],the actual is {numbers_ins19}"
)
print(
    f"initial array is {numbers}, after iserting 20 the expected list is\
[10, 10, 10, 20, 20, 20, 20, 30, 30, 40],the actual is {numbers_ins20}"
)
print(
    f"initial array is {numbers}, after iserting 7 the expected list is\
[10, 10, 10, 20, 20, 20, 30, 30, 40, 45],the actual is {numbers_ins45}"
)
