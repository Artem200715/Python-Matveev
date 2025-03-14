# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Сумма элементов:
# Элементы до n-1 умножены на элемент n:

l = ['-50 -25 0 25 50']

file = open('matveev.txt', 'w', encoding="utf-8")
file.writelines(l)
file.close()
file1 = open('matveev1.txt', 'w', encoding="utf-8")
file1.writelines('Исходные данные: ')
file1.writelines(l)
file1.write('\n')
file1.close()
file = open('matveev.txt')
k = file.read()
k = k.split()
for i in range(len(k)):
 k[i] = int(k[i])
file.close()
file1 = open('matveev1.txt', 'a', encoding="utf-8")
file1.writelines('ааагугугага: ')
file1.write('\n')
file1.writelines(len(k))
file1 = open('matveev1.txt', 'a', encoding="utf-8")
file1.writelines('Количество элементов: ')
file1.write('\n')
file1.close()