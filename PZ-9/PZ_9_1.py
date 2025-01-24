# Организовать словарь avto, содержащий 3 ключа (марки авто) и списки
# из трех моделей в качестве значений. Обеспечить отображение вторых моделей по
# каждому авто, всех моделей словаря.

avto = {'BMW': ["iX M60", "i7", "i4 M50 xDrive"], 'Wolksvagen': ["Tiguan", "Passat", "Polo"], 'Skoda': ["Octavia", "Fabia", "Rapid"]}

for key in avto:
    mark = avto.get(key)
    print(key, mark[1])


print(avto['BMW'])
print(avto['Wolksvagen'])
print(avto['Skoda'])
