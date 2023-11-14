# Одна таблица + сортировка
import sqlite3

con = sqlite3.connect("B_db.db")  # input()
cur = con.cursor()
A, B = 10, 1
result = cur.execute("""SELECT price, number, name FROM Test
                        WHERE price < ? OR number > ?""", (A, B)).fetchall()
print(sorted(result, reverse=True))
s = '%a_'
results = cur.execute("""SELECT * FROM Test
                        WHERE name LIKE ?""", (s,)).fetchall()
result = cur.execute("""SELECT name FROM Test
                        WHERE name LIKE ?""", (s,)).fetchone()
print(results, result, result[0])
# [('bread', 2.0, 6)] ('bread',) bread