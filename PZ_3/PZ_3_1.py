# Проверить истинность высказывания: «Среди трех данных целых чисел есть хотя бы
# одна пара совпадающих».

number1, number2, number3 = input('Введите первое число'), input('Введите второе число'), input('Введите третье число')

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
while type(number3) != int:
    try:
        number3 = int(number3)
    except ValueError:
        print('Неправильно Ввели!')
        number3 = input('Введите третье число')


if number1 == number2 or number2 == number3 or number1 == number3:
    print("Из этих чисел как минимум два равны между собой")
else:
    print("Из этих чисел нет ни одного равного")