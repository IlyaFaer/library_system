import random

rand_list = [random.randint(1, 20) for _ in range(10)]

list_comprehension_below_10 = [i for i in rand_list if i < 10]

list_comprehension_below_10 = list(filter(lambda i: i < 10, rand_list))

print(rand_list)
print(list_comprehension_below_10)
