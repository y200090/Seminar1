from dotenv import load_dotenv
import os, requests, json, sys
import pandas as pd

load_dotenv()
api_key = os.getenv('API_KEY')

keyword = input('keyword: ')

url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={keyword}&apikey={api_key}'
res = requests.get(url)
data = res.json()

print(json.dumps(data, indent=2))
