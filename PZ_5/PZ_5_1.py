# Составить функцию решения задачи: из заданного числа вычли сумму его цифр. Из
# результата вновь вычли сумму его цифр и т. д. Через сколько таких действий
# получится нуль?


def task(n):
    steps = 0

    while n != 0:
        chislo = sum(int(digit) for digit in str(n))

        n -= chislo

        steps += 1

    return steps

n = input("Введите число: ")

while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print("Неправильно ввели!")
        n = input("Введите число: ")

result = task(n)

print(result)


