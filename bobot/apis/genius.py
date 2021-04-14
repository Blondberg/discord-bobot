import requests
import os
from dotenv import load_dotenv
from requests.api import request
import json


class GeniusAPI:
    def __init__(self):
        load_dotenv()
        self.GENIUS_TOKEN = os.getenv("GENIUS_TOKEN")
        self.GENIUS_CLIENT_ID = os.getenv("GENIUS_CLIENT_ID")
