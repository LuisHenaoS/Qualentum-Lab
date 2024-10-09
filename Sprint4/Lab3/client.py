
import requests
import sys

BASE_URL = 'http://127.0.0.1:8080'

def add_entry(entry):
    url = f"{BASE_URL}/add_entry"
    response = requests.post(url, json={"entry": entry})
    if response.status_code == 201:
        print(f"Success: {response.json()['message']}")
    else:
        print(f"Failed: {response.json()['error']}")

def fetch_entries():
    url = f"{BASE_URL}/fetch_entries"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json().get('data', [])
        print("Entries in the database:")
        for i, entry in enumerate(data, 1):
            print(f"{i}. {entry}")
    else:
        print(f"Failed to retrieve entries: {response.json()['error']}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python client.py [add|fetch] [entry_data_if_add]")
    elif sys.argv[1] == 'add' and len(sys.argv) == 3:
        add_entry(sys.argv[2])
    elif sys.argv[1] == 'fetch':
        fetch_entries()
    else:
        print("Invalid command. Use 'add' or 'fetch'.")
