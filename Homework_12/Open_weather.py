import json
import os
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


def get_api_key():
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if api_key:
        return api_key

    env_file = Path(__file__).with_name(".env")
    try:
        lines = env_file.read_text(encoding="utf-8").splitlines()
    except FileNotFoundError:
        return None
    except OSError as error:
        print(f"Could not read the .env file: {error}", file=sys.stderr)
        return None

    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue

        name, separator, value = line.partition("=")
        if separator and name.strip() == "OPENWEATHER_API_KEY":
            value = value.strip()
            if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
                value = value[1:-1]
            return value or None

    return None


def main():
    city = input("Enter a municipality: ").strip()
    if not city:
        print("Please enter a municipality.", file=sys.stderr)
        return

    api_key = get_api_key()
    if not api_key:
        print(
            "Set OPENWEATHER_API_KEY in the environment or in "
            "Homework_12/.env before running this program.",
            file=sys.stderr,
        )
        return

    query = urlencode({"q": city, "appid": api_key})
    request = Request(
        f"https://api.openweathermap.org/data/2.5/weather?{query}",
        headers={"User-Agent": "Mozilla/5.0", "Accept": "application/json"},
    )

    try:
        with urlopen(request, timeout=10) as response:
            weather = json.load(response)
        description = weather["weather"][0]["description"]
        temperature_kelvin = weather["main"]["temp"]
        temperature_celsius = temperature_kelvin - 273.15
    except HTTPError as error:
        if error.code == 401:
            message = "OpenWeather rejected the API key. Check that it is valid and active."
        elif error.code == 404:
            message = f"Municipality '{city}' was not found."
        else:
            message = f"OpenWeather returned HTTP {error.code}."
        print(message, file=sys.stderr)
        return
    except (URLError, TimeoutError) as error:
        print(f"Could not connect to OpenWeather: {error}", file=sys.stderr)
        return
    except (json.JSONDecodeError, KeyError, IndexError, TypeError):
        print("Received invalid weather data from OpenWeather.", file=sys.stderr)
        return

    print(f"Weather: {description}")
    print(f"Temperature: {temperature_celsius:.1f} °C")


if __name__ == "__main__":
    main()