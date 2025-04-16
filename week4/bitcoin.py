import sys
import requests

API_KEY = "YOUR_API_KEY"
URL = f"http://rest.coincap.io/v3/assets/bitcoin?apiKey=YOUR_API_KEYASD"


def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get(URL)
        response.raise_for_status()
        data = response.json()
        price = float(data["data"]["priceUsd"])
        total = bitcoins * price
        print(f"${total:,.4f}")
    except requests.RequestException:
        sys.exit("Error fetching Bitcoin price")


if __name__ == "__main__":
    main()
