# Организовать словарь avto, содержащий 3 ключа (марки авто) и списки
# из трех моделей в качестве значений. Обеспечить отображение вторых моделей по
# каждому авто, всех моделей словаря.

avto = {1: ["iX M60", "i7", "i4 M50 xDrive"], 2: ["Tiguan", "Passat", "Polo"], 3: ["Octavia", "Fabia", "Rapid"]}

k = 1
while k != 4:
    mark = avto.get(k)
    print(mark[1])
    k += 1
k = 1
while k != 4:
    print(avto.get(k))
    k += 1
