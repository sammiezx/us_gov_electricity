import requests
import pandas as pd
import os
from dotenv import load_dotenv

def hit_gov_data(start_date='2001-01', end_date='2023-01', offset=0, length=5000):
    load_dotenv()
    api_key = os.getenv("GOV_API_KEY")

    api_url = f"https://api.eia.gov/v2/electricity/retail-sales/data/?api_key={api_key}&frequency=monthly&data[0]=customers&data[1]=price&data[2]=revenue&data[3]=sales&start={start_date}&end={end_date}&sort[0][column]=period&sort[0][direction]=desc&offset={offset}&length={length}"
    # api_url = "https://api.eia.gov/v2/electricity/retail-sales/data/?frequency=monthly&data[0]=customers&data[1]=price&data[2]=revenue&data[3]=sales&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000"
    response = requests.get(api_url)
    if response.status_code == 200:
        return pd.DataFrame(response.json()['response']['data'])
    else:
        raise Exception("ISSUE HITTING US GOVERMENT DATA API")