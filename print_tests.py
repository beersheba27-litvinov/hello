from functions import merge_in_place
from unittest_print import print_results, print_test

numbers_abs = [3, 5, 7, -11, 0, 4, -10, -20, 100, -80, -4, 8]
numbers = [-11, 3, 5, 7, -20, -10, 0, 4, 100, -80, -4, 8]
numbers_act = numbers.copy()

numbers_abs_exp = [0, 3, 4, 5, 7, -10, -11, -20, 100, -80, -4, 8]
numbers_exp = [-20, -11, -10, 0, 3, 4, 5, 7, 100, -80, -4, 8]
numbers_abs_act = numbers_abs.copy()
merge_in_place(numbers_act, start=0, len1=4, size=8)
merge_in_place(numbers_abs_act, start=0, len1=4, size=8, key=abs)

print_test(
    f"merge subparts of the first 8 numbers in the list {numbers} ",
    numbers_exp,
    numbers_act,
)
print_test(
    f"merge subparts of the first 8 numbers in the list {numbers_abs} according to the abs values ",
    numbers_abs_exp,
    numbers_abs_act,
)


print_results()
