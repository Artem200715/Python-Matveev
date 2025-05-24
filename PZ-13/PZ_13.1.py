# В двумерном списке найти среднее арифметическое элементов последних двух
# столбцов.
from functools import reduce
import random
number = [[random.randint(1, 10) for x in range(1, 4)] for y in range(random.randint(3, 5))]
print("Список: ", number)
answ = []

for i in number:
    answ += i[1:3][i]

summ = reduce(lambda x, y: x+y, answ)
print("Сумма последних 2 столбцов: ", summ)
mid = summ / len(answ)
print("Среднее арифметическое элементов двух последних столбцов", mid)
