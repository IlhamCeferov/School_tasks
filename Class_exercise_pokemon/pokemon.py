import json
from urllib.error import  HTTPError, URLError
from urllib.request import urlopen

def main():
    name = input("Enter the name of a Pokemon: ").strip()

    if not name:
        print("Please enter a Pokemon name. ")
        return

    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"

    try:
        with urlopen(url, timeout=10) as response:
            pokemon = json.load(response)
    except HTTPError as error:
        if error.code == 404:
            print(f"Pokemon '{name}' was not found. ")
        else:
            print(f"Search failed with HTTP status {error.code}.")
        return
    except (URLError, TimeoutError):
        print("Could not connect to the Pokemon service. ")
        return
    except (json.JSONDecodeError, KeyError, TypeError):
        print("Received invalid data from the Pokemon service. ")
        return

    types = [entry["type"]["name"] for entry in pokemon["types"]]
    print(f"{name}: {','.join(types)}")

if __name__ == "__main__":
    main()