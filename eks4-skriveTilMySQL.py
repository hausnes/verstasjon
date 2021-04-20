import mysql.connector
# NB: Denne må installerast litt ulikt guiden frå W3, som antar du sit i Windows:
# sudo apt-get -y install python3-mysql.connector
# Deretter er all koden lik.

mydb = mysql.connector.connect(
	host="",
	user="",
	password="",
	database=""
)

mycursor = mydb.cursor()

sql = "INSERT INTO user_accounts (userid, firstname, lastname, phone) VALUES (%s, %s, %s, %s)"
val = ("HAL", "Hilde", "Larsen", "92047938")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")