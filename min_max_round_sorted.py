numbers = [3, 4, 5.5, 45.2, 36.4, 65.6, 1, 19]
print("Original List: {}".format(numbers))
number = list(map(round, numbers))
print("Minimum value: ", min(numbers))
print("Maximum value: ", max(numbers))
number = list(set(number))
number = sorted(map(lambda n: n * 5, number))
print("result")
for x in number:
    print(x, end=' ')
