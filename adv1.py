# ===============最終発展課題1 12/1===============

import requests, time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

service = ChromeService(ChromeDriverManager().install())
options = Options().add_argument('start-maximized')
driver = webdriver.Chrome(service=service, options=options)
driver.get('https://google.com/')


# urls = [
#     "https://news.yahoo.co.jp/",
#     "http://www.pretend_server.org",
#     "https://github.co.jp/",
#     "https://github.co.jp/y200090jp"
# ]

# for i, url in enumerate(urls):
#     try:
#         print(f'URL: {url}')
#         res = requests.get(url)
#         res.raise_for_status()
#         with open(f'scraping/res-{i}.html', 'w', encoding='utf-8') as f:
#             f.write(res.text)
#     except requests.exceptions.RequestException as err:
#         print(f'>>> \033[31m{err}\033[0m\n')
#     else:
#         print('>>> 正常にスクレイピングが完了しました。\n')
