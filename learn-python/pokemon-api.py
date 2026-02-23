import requests
from dotenv import load_dotenv, find_dotenv
import os
import json

load_dotenv(find_dotenv())

API_PATH = os.getenv("API_PATH")

if not API_PATH:
    raise Exception("no API_PATH found")

def search_pokemon():
    try:
        user_pokemon = input("Enter the pokemon: ").strip().lower()
        pokemon = requests.get(f"{API_PATH}/pokemon/{user_pokemon}").json()
        print(type(pokemon))
        with open(f"{user_pokemon}.json", "w") as f:
            json.dump(pokemon, f, indent=2)
            f.close()
    except Exception as error:
        print(error)

def get_pokemon():
    try:
        pokemon = input("Enter pokemon to search: ")
        with open(f"{pokemon}.json") as f:
            returned_pokemon = json.load(f)
            print(type(returned_pokemon))
    except Exception as error:
        print(error)

get_pokemon()