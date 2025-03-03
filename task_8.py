nums = [12, 15, 18, 20, 24, 30]
jijoid = list(map(lambda x: x + 5, filter(lambda x: x % 6 == 0, nums)))
print(jijoid)