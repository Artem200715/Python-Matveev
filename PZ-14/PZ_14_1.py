#   Из исходного текстового файла (pazzl.html) выбрать все html-коды изображений.
#   Посчитать их количество.
import re
p = r"<img\b[^>]*>"

f = open("pazzl.html", "r", encoding="utf-8")
linda = f.read()
img = re.findall(p, linda)
f.close()
print(img)
print(len(img))


