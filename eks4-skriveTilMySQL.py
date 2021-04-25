import mysql.connector

''' 
	NB: mysql.connector må installerast litt ulikt guiden frå W3, som antar du sit i Windows:
	
	Alternativ 1: 
	pip3 install mysql-connector-python (eventuelt pip, altså utan 3-talet)
	
	Alternativ 2: 
	sudo apt-get -y install python3-mysql.connector
	
	Deretter er all koden lik.
	Før du forsøker med den resterande koden så sjekkar du om programmet køyrer berre ved å ha linje 1, med import.
'''

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