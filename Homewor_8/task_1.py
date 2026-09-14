import mysql.connector

icao_code = input("ICAO code of the airport: ").upper()

connection = mysql.connector.connect(
    host = "localhost",
    database = "flight_game",
    user = "root",
    password = "Nergiz2017"
)

cursor = connection.cursor()
cursor.execute("SELECT name, municipality FROM airport WHERE ident = %s",
               (icao_code,))

airport = cursor.fetchone()

if airport:
    print(f"Airport: {airport[0]}")
    print(f'Location: {airport[1]}')
else:
    print("Airport not found.")

cursor.close()
connection.close()
