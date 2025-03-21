# В двумерном списке найти среднее арифметическое элементов последних двух
# столбцов.
from functools import reduce
number = [[1, 6, 2],
          [2, 4, 0],
          [8, 7, 5]]

answ = []

for i in number:
    answ += i[1:3]

print(reduce(lambda x, y: x+y, answ))
