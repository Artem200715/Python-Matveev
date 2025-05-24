# Приложение ГРУЗОВЫЕ ПЕРЕВОЗКИ для некоторой организации. БД должна
# содержать таблицу Перевозки со следующей структурой записи: маршрут, фамилия
# водителя, даты отправки и прибытия, масса груза.
import sqlite3 as sq

with sq.connect("baza.db") as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS perevozki (
    per_id INTEGER PRIMARY KEY NOT NULL,
    start_address VARCHAR(30),
    end_address VARCHAR(30),
    driver_ln VARCHAR(20),
    start_date DATE,
    end_date DATE,
    weight INTEGER NOT NULL
    )""")
with sq.connect("baza.db") as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM perevozki WHERE weight = 200")
    result = cur.fetchall()
    print("Вывести все строчки, где груз весит 200 кг", result)
with sq.connect("baza.db") as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM perevozki WHERE driver_ln = 'Матвеев'")
    result1 = cur.fetchone()
    result2 = cur.fetchmany(2)
    print("Вывести первую строчку с фамилией Матвеев", result1)
    print("Вывести следующие две строчки с фамилией Матвеев", result2)
