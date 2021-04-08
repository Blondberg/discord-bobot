import requests
import os
from dotenv import load_dotenv

load_dotenv()
RIOT_TOKEN = os.getenv('RIOT_KEY')

def data_version():
    """Get current data version for Data Dragon

    Returns:
        string: The newest version of the data
    """
    ddragon = "https://ddragon.leagueoflegends.com/realms/euw.json"
    euw_json = requests.get(ddragon).json()
    return euw_json['n']['champion']

url = f'http://ddragon.leagueoflegends.com/cdn/{data_version()}/data/en_US/champion.json'


def get_champions():
    data_json = requests.get(url).json()
    champions = list(data_json['data'].keys())
    return champions
