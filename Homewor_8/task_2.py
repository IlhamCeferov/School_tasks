import mysql.connector

area_code = input("Enter area code: ").upper()

connection = mysql.connector.connect(
    host = "localhost",
    database = "flight_game",
    user = "root",
    password = "Nergiz2017"
)

cursor = connection.cursor()

query = """
    SELECT type, name 
    FROM airport 
    WHERE iso_country = %s 
    ORDER BY type
"""

cursor.execute(query, (area_code,))

for airport_type, airport_name in cursor:
    print(f"{airport_type}: {airport_name}")

cursor.close()
connection.close()