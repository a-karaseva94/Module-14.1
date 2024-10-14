import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users(email)")

# for i in range(1, 11):
#     cursor.execute("INSERT INTO Users (username, email, age, balance) "
#                    "VALUES (?, ?, ?, ?)", (f"User{i}", f"example{i}@gmail.com", f"{i * 10}", "1000"))


# Обновление balance у каждой 2ой записи начиная с 1ой на 500:

# for i in range(1, 11):
#     if i % 2 == 0:
#         pass
#     else:
#         cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500, f"User{i}"))


# Удаление каждой 3ей записи в таблице начиная с 1ой:

# cursor.execute("DELETE FROM Users WHERE id IN (1, 4, 7, 10)")


# выбор всех записей

# cursor.execute("SELECT * FROM Users WHERE age != ?", (60,))
# users = cursor.fetchall()
# for data in users:
#     print(f" Имя: {data[1]} | Почта: {data[2]} | Возраст: {data[3]} | Баланс: {data[4]}")


connection.commit()
connection.close()