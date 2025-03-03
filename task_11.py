nums = list(range(1, 11)) # я устал
нечеткие = list(filter(lambda x: x % 2 != 0, nums))
получеткие = list(map(lambda x: x + 10 if x in нечеткие else x, nums))
print(получеткие)