import json
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def main():
    request = Request(
        "https://api.chucknorris.io/jokes/random",
        headers={"User-Agent": "Mozilla/5.0", "Accept": "application/json"},
    )

    try:
        with urlopen(request, timeout=10) as response:
            joke = json.load(response)["value"]
    except HTTPError as error:
        print(f"Chuck Norris API returned HTTP {error.code}.", file=sys.stderr)
        return
    except (URLError, TimeoutError) as error:
        print(f"Could not connect to the Chuck Norris API: {error}", file=sys.stderr)
        return
    except (json.JSONDecodeError, KeyError, TypeError):
        print("Received an invalid response from the Chuck Norris API.", file=sys.stderr)
        return

    print(joke)


if __name__ == "__main__":
    main()