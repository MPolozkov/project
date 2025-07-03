import os
from typing import List, Dict
import requests

from dotenv import load_dotenv

load_dotenv()


def conversions(symbols: str, base: str, token=os.getenv('API_KEY')) -> float:
    url = f"https://api.apilayer.com/exchangerates_data/latest?symbols={symbols}&base={base}"
    headers = {"apikey": token}
    response = requests.request("GET", url, headers=headers)
    response.raise_for_status()
    data = response.json()
    return data['rates'][symbols]
