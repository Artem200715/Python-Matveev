# Создайте класс «Студент», который имеет атрибуты имя, фамилия и оценки.
# Добавьте методы для вычисления среднего балла и определения, является ли студент
# отличником.

class Student():
    def __init__(self, name, ln, marks):
        self.name = name
        self.ln = ln
        self.marks = marks
    
    def mid(self):
        marks = sum(self.marks) / len(self.marks)
        return marks
    
    def is_cool(self):
        print("Он отличник!" if self.mid() >= 4.5 else "Не отличник!")

stud = Student("Артём", "Матвеев", [4, 5, 5, 5, 4, 4, 5])
print("Студент:", stud.name, stud.ln)
print("Средний балл:", stud.mid())
stud.is_cool()