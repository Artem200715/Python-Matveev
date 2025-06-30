import tkinter as tk
from tkinter import messagebox


def calculate():
    number = entry.get()

    if len(number) != 3 or not number.isdigit():
        messagebox.showerror("Ошибка", "Пожалуйста, введите трехзначное число")
        return

    digits = [int(d) for d in number]
    digit_sum = sum(digits)
    digit_product = 1
    for d in digits:
        digit_product *= d

    result_label.config(text=f"Сумма цифр: {digit_sum}\nПроизведение цифр: {digit_product}")


# Создаем главное окно
root = tk.Tk()
root.title("Трехзначное число")
root.geometry("300x200")

# Создаем элементы интерфейса
label = tk.Label(root, text="Введите трехзначное число:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="Вычислить", command=calculate)
button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Запускаем главный цикл
root.mainloop()