from functools import reduce
num = [1, 5, 2, 1, 7, 12, 4, 3, 9]
# x = 0
# for i in range(0, 3):
#    x += num[i]
x = 0
answ = [x + num[i] for i in range(0, 3)]
nums = reduce(lambda z, y: z + y, answ)
print(nums)
