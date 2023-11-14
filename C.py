# Несколько таблиц со связями,
# сложный запрос + сортировка
import sqlite3

con = sqlite3.connect("C_db.db")  # input()
cur = con.cursor()
result = cur.execute("""SELECT Product.name, Customer.name From Orders
Join Product on Orders.product_id = Product.id
Join Customer on Orders.customer_id = Customer.id
Where Orders.number < 2
ORDER BY Customer.name""").fetchall()
for item in result:
    print(item)
