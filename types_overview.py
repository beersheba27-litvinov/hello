import random


def create_random_list(min, max, size):
    res = []
    for i in range(size):
        res.append(random.randint(min, max))
    return res


print(create_random_list(1, 10, 3))
