import os

import mysql.connector
from flask import Flask, jsonify


app = Flask(__name__)


def find_airport(icao_code: str) -> tuple[str | None, str | None] | None:
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    if not user or password is None:
        raise RuntimeError("Set DB_USER and DB_PASSWORD before starting the service.")

    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        database=os.getenv("DB_NAME", "flight_game"),
        user=user,
        password=password,
    )
    try:
        cursor = connection.cursor()
        try:
            cursor.execute(
                "SELECT name, municipality FROM airport WHERE ident = %s",
                (icao_code,),
            )
            airport = cursor.fetchone()
            if airport is None:
                return None
            return airport[0], airport[1]
        finally:
            cursor.close()
    finally:
        connection.close()


@app.get("/airport/<icao_code>")
def airport_info(icao_code: str):
    icao_code = icao_code.upper()
    airport = find_airport(icao_code)
    if airport is None:
        return jsonify({"error": "Airport not found"}), 404

    name, location = airport
    return jsonify({"ICAO": icao_code, "Name": name, "Location": location})


if __name__ == "__main__":
    app.run()