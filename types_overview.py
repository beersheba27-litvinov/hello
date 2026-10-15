import random

age = random.randint(1, 100)
print("age =", age)
if age < 13:
    print("child")
elif age < 20:
    print("junior")
elif age < 67:
    print("adult")
else:
    print("pensioner")
