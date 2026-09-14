import mysql.connector
from geopy.distance import geodesic

first_icao = input("Enter the ICAO code of the first airport: ").upper()
second_icao = input("Enter the ICAO code of the second airport: ").upper()

connection = mysql.connector.connect(
    host = "localhost",
    database = "flight_game",
    user = "root",
    password = "Nergiz2017"
)

cursor = connection.cursor()

query = """
    SELECT latitude_deg, longitude_deg
    FROM airport
    WHERE ident = %s
"""

cursor.execute(query, (first_icao,))
first_airport = cursor.fetchone()

cursor.execute(query, (second_icao,))
second_airport = cursor.fetchone()

if first_airport is None or second_airport is None:
    print("One or both airports not found.")
else:
    first_coordinates = (first_airport[0], first_airport[1])
    second_coordinates = (second_airport[0], second_airport[1])

    distance = geodesic(first_coordinates, second_coordinates).kilometers
    print(f"The distance between the airports is {distance:.2f} kilometers.")

cursor.close()
connection.close()

    