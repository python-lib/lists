import random


def three_random_numbers(num_list, num):
    return random.sample(num_list, num)


num_list = [2, 3, 4, 5, 34, 2, 2, 34, 54, 32]
print("==========Original List=============")
print(num_list)
select_nums = 3
result = three_random_numbers(num_list, select_nums)
print("===========The selected three nums===========")
print(result)
