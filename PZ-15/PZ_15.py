# Приложение ГРУЗОВЫЕ ПЕРЕВОЗКИ для некоторой организации. БД должна
# содержать таблицу Перевозки со следующей структурой записи: маршрут, фамилия
# водителя, даты отправки и прибытия, масса груза.
import sqlite3 as sq

values = [
    [1, 'Ростов', 'Казань', 'Матвеев', '20.01.2007', '22.01.2008', 200],
    [2, 'Ростов', 'Казань', 'Баранов', '20.01.2007', '22.01.2008', 250],
    [3, 'Ростов', 'Казань', 'Олегов', '20.01.2007', '22.01.2008', 150],
    [4, 'Ростов', 'Ставрополь', 'Матвеев', '25.01.2007', '30.01.2008', 400],
    [5, 'Ростов', 'Ставрополь', 'Баранов', '25.01.2007', '30.01.2008', 305],
    [6, 'Ростов', 'Ставрополь', 'Олегов', '25.01.2007', '30.01.2008', 199],
    [7, 'Ростов', 'Орел', 'Матвеев', '02.02.2007', '09.02.2008', 1000],
    [8, 'Ростов', 'Орел', 'Олегов', '02.02.2007', '09.02.2008', 199],
    [9, 'Ростов', 'Орел', 'Баранов', '02.02.2007', '09.02.2008', 900],
    [10, 'Ростов', 'Алматы', 'Матвеев', '15.02.2007', '16.02.2008', 1100]
]

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

# with sq.connect("baza.db") as con:
#    cur = con.cursor()
#    cur.executemany("INSERT INTO perevozki VALUES (?, ?, ?, ?, ?, ?, ?)", values)
with sq.connect("baza.db") as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM perevozki WHERE weight = 200")
    result = cur.fetchall()
    print("Вывести все строчки, где груз весит 200 кг:", result)
with sq.connect("baza.db") as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM perevozki WHERE driver_ln = 'Матвеев'")
    result1 = cur.fetchall()
    print("Вывести первую строчку с фамилией Матвеев:", result1)
with sq.connect("baza.db") as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM perevozki WHERE weight > 200")
    result2 = cur.fetchall()
    print("Вывести строчки с весом больше 200:", result2)
# with sq.connect("baza.db") as con:
#    cur = con.cursor()
#    cur.execute("DELETE FROM perevozki WHERE driver_ln = 'Матвеев'")
# with sq.connect("baza.db") as con:
#    cur = con.cursor()
#    cur.execute("DELETE FROM perevozki WHERE weight < 200")
# with sq.connect("baza.db") as con:
#    cur = con.cursor()
#    cur.execute("DELETE FROM perevozki WHERE driver_ln = 'Баранов'")
# with sq.connect("baza.db") as con:
#    cur = con.cursor()
#    cur.execute("UPDATE perevozki  SET weight = 500 WHERE weight = 1000")
# with sq.connect("baza.db") as con:
#    cur = con.cursor()
#    cur.execute("UPDATE perevozki  SET weight = 250 WHERE weight = 1100")
# with sq.connect("baza.db") as con:
#    cur = con.cursor()
#    cur.execute("UPDATE perevozki  SET driver_ln = 'Матвиив' WHERE driver_ln = 'Матвеев'")