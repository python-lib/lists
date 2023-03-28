def only_odds():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 20]
    nums = [x for x in nums if x % 2 != 0]
    print(nums)
