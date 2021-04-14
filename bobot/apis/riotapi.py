import requests
import os
from dotenv import load_dotenv
from requests.api import request
import json

load_dotenv()
RIOT_TOKEN = os.getenv("RIOT_KEY")


def get_data_version(data: str, server: str):
    ddragon_url = f"https://ddragon.leagueoflegends.com/realms/{server}.json"
    server_data_json = requests.get(ddragon_url).json()
    return server_data_json["n"][data]


def get_data_json(data: str, server="euw"):
    url = f"http://ddragon.leagueoflegends.com/cdn/{get_data_version(data, server)}/data/en_US/{data}.json"
    data_json = requests.get(url).json()
    return data_json
    """
    data_list = list(data_json['data'].keys())
    return data_list
    """


def get_champions():
    try:
        with open(
            os.path.join(os.path.dirname(__file__), "data/leaguechampions.json"), "r"
        ) as f:
            champions_json = json.load(f)
        return list(champions_json["data"].keys())
    except FileNotFoundError:
        fetch_data()
        return get_champions()


def fetch_data():
    print("Fetching data from the Riot Games API...")
    champions_json = get_data_json("champion", "euw")
    with open(
        os.path.join(os.path.dirname(__file__), "data/leaguechampions.json"), "w"
    ) as f:
        json.dump(champions_json, f)
