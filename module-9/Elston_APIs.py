#Tanner Elston, 11/26/2025, APIs Module 9


"""
API Tutorial Program

Part 1: Open Notify Astronauts API
Part 2: Chuck Norris Joke API
"""

import requests

ASTROS_URL = "http://api.open-notify.org/astros.json"
CHUCK_URL = "https://api.chucknorris.io/jokes/random"


def test_connection(url, description):
    print(f"\nTesting connection to {description}: {url}")
    try:
        response = requests.get(url, timeout=10)
        print(f"Status code: {response.status_code}")
        response.raise_for_status()
        print("Connection successful.")
        return response
    except requests.exceptions.RequestException as e:
        print("Connection failed:", e)
        return None


def show_astronauts():
    print("=" * 65)
    print(" CURRENT ASTRONAUTS (Open Notify API) ")
    print("=" * 65)

    response = test_connection(ASTROS_URL, "Open Notify Astronauts API")
    if response is None:
        return

    print("\nRaw response:")
    print(response.text)

    data = response.json()
    print("\nFormatted output:")
    print(f"Message: {data.get('message')}")
    print(f"Number of people in space: {data.get('number')}\n")

    for person in data.get("people", []):
        print(f" - {person.get('name')} aboard {person.get('craft')}")


def show_chuck():
    print("\n" + "=" * 65)
    print(" Chuck Norris Random Joke API ")
    print("=" * 65)

    response = test_connection(CHUCK_URL, "Chuck Norris Joke API")
    if response is None:
        return

    print("\nRaw response:")
    print(response.text)

    data = response.json()
    print("\nFormatted output:")
    print("Random Chuck Norris Fact:")
    print(f"  {data.get('value')}")


if __name__ == "__main__":
    show_astronauts()
    show_chuck()
