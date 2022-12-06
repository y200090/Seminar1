from dotenv import load_dotenv
import os, requests, json, sys
import pandas as pd

load_dotenv()
api_key = os.getenv('API_KEY')

args = sys.argv[1]

if args == 'f':
    url = f'https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=USD&to_symbol=JPY&interval=15min&outputsize=full&apikey={api_key}'
    res = requests.get(url)
    data = res.json()
    data = data['Time Series FX (Daily)']
    # print(json.dumps(data, indent=2))

    fx_data = []
    for (i, df) in enumerate(data):
        col = []
        fx = data
        col.append(df)                    # 日時
        col.append(fx[df]['1. open'])     # 始値
        col.append(fx[df]['2. high'])     # 高値
        col.append(fx[df]['3. low'])      # 安値
        col.append(fx[df]['4. close'])    # 終値
        fx_data.append(col)

    fx_df = pd.DataFrame(fx_data)
    fx_df = fx_df.set_axis(['Datetime','open', 'high', 'low', 'close'], axis=1)
    print(fx_df)

# リアルタイムの為替レートを取得
if args == 'e':
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=JPY&apikey={api_key}'
    res = requests.get(url)
    data = res.json()
    data = data['Realtime Currency Exchange Rate']
    print(json.dumps(data, indent=2))   # 9時間プラスで日本時間

if args == 'i':
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=USDJPY&interval=5min&outputsize=full&apikey={api_key}'
    r = requests.get(url)
    data = r.json()
    data = data['Time Series (5min)']
    print(json.dumps(data, indent=2))   # 13時間プラスで日本時間
