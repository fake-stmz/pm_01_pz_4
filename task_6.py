nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
slain_by_cinq_association = list(filter(lambda x: x % 5 == 0, nums))
print(slain_by_cinq_association)