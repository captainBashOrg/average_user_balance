import sqlite3

connection_DB = sqlite3.connect ( 'not_only_telegram.db' )
cursor = connection_DB.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email   TEXT NOT NULL,
age INTEGER,
balance INTEGER
)
'''
)
# индекс по возрасту и балансу -- не повредит
cursor.execute("CREATE INDEX IF NOT EXISTS idx_age ON Users (age, balance)")


for i in range (1, 11):
    cursor.execute(" INSERT INTO Users (username,  email, age, balance) VALUES (?, ?, ?, ?)", (f"User{i}",   f"example{i}@gmail.com", i*10, i*1000))


cursor.execute('SELECT * FROM Users  ')
rows = cursor.fetchall()


#Обновите balance у каждой 2ой записи начиная с 1ой на 500:
for i in range(1, 11, 2):
    cursor.execute('UPDATE Users SET balance = ? WHERE username = ?', (500, f'User{i}'))

#Удалите каждую 3ую запись в таблице начиная с 1ой:
for i in range(1, 11, 3):
    cursor.execute('DELETE FROM Users WHERE username = ?', (f'User{i}',))
print("Удалили каждую 3ую запись в таблице начиная с 1ой")
for row in rows:
    print(f"ID:{row [0]} Имя: {row [1]} | Почта: {row [2]} | Возраст: {row [3]} | Баланс: {row [4]}")



#Сделайте выборку всех записей при помощи fetchall(), где возраст не равен 60 и выведите их в консоль в следующем формате (без id):
# Имя: <username> | Почта: <email> | Возраст: <age> | Баланс: <balance>
cursor.execute('SELECT * FROM Users WHERE age != 60')
rows = cursor.fetchall()
print("возраст не равен 60 ")
for row in rows:
    print(f"ID:{row [0]} Имя: {row [1]} | Почта: {row [2]} | Возраст: {row [3]} | Баланс: {row [4]}")


cursor.execute('SELECT * FROM Users  ')
rows = cursor.fetchall()

for row in rows:
    print(f"ID:{row [0]} Имя: {row [1]} | Почта: {row [2]} | Возраст: {row [3]} | Баланс: {row [4]}")

#Удалите из базы данных not_telegram.db запись с id = 6.
cursor.execute("DELETE FROM Users WHERE id = ?", (6,))

print("Удалили 6-ю запись")
cursor.execute('SELECT * FROM Users  ')
rows = cursor.fetchall()

for row in rows:
    print(f"ID:{row [0]} Имя: {row [1]} | Почта: {row [2]} | Возраст: {row [3]} | Баланс: {row [4]}")

#Подсчитать общее количество записей.
cursor.execute("SELECT COUNT(*) FROM Users" )
qTy = cursor.fetchone()[0]
print(f"Общее количество записей {qTy}")

#Посчитать сумму всех балансов.
cursor.execute("SELECT SUM(balance) FROM Users" )
summ = cursor.fetchone()[0]
print(f"Cумма всех балансов {summ}")


#Вывести в консоль средний баланс всех пользователей.
print(f"Cредний баланс всех пользователей {summ / qTy  }")


    #    cursor.execute('SELECT AVG(balance)  FROM Users')
#    rows = cursor.fetchall()[0]
#    print(rows)
#    cursor.execute('SELECT AVG(balance)  FROM Users')
#    rows = cursor.fetchone()
#    print(rows)

connection_DB.commit()
connection_DB.close()
