# Перенести в новый двумерный список Matr1 элементы, которые не находятся в
# первых и последних сроках и столбцах матрицы Matr2 произвольного размера.
import random

Matr2 = [[random.randint(1, 10) for x in range(1, 6)] for y in range(random.randint(3, 5))]
print("Изначальный список: ", Matr2)
Matr2.pop(0)
Matr2.pop(-1)
print("Сначала убираем первые и последние строки: ", Matr2)


def ok(n):
    for i in n:
        i.pop(0)
        i.pop(-1)
        yield i


Matr1 = list(ok(Matr2))

print("Элементы которые мы перенесли в другой список: ", Matr1)
