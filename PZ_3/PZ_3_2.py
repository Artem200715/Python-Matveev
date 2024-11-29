# Даны две переменные целого типа: A и B. Если их значения не равны, то присвоить
# каждой переменной сумму этих значений, а если равны, то присвоить переменным
# нулевые значения. Вывести новые значения переменных A и B.

number1, number2 = input('Введите первое число'), input('Введите второе число')

while type(number1) != int:
    try:
        number1 = int(number1)
    except ValueError:
        print('Неправильно Ввели!')
        number1 = input('Введите первое число')
while type(number2) != int:
    try:
        number2 = int(number2)
    except ValueError:
        print('Неправильно Ввели!')
        number2 = input('Введите второе число')
if number1 != number2:
    number3 = number1+number2
    number4 = number1+number2
else:
    number3 = 0
    number4 = 0

print(number3, number4)
