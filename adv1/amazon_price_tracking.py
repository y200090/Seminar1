# ===============最終発展課題1 12/1===============

from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = ChromeService(ChromeDriverManager().install())

def amazon_page(url):
    driver = webdriver.Chrome(service=service)
    driver.get(url)
    driver.implicitly_wait(10)
    text = driver.page_source
    driver.quit()
    return text

if __name__ == "__main__":
    urls = [
        "https://www.amazon.co.jp/dp/B0B14HRL16/ref=sspa_dk_detail_0?psc=1&pf_rd_p=96b07241-deb4-4034-babe-8423591f6bfe&pf_rd_r=5GKGJCF4RCWRD8YNYX3D&pd_rd_wg=9ivXd&pd_rd_w=9ul2A&content-id=amzn1.sym.96b07241-deb4-4034-babe-8423591f6bfe&pd_rd_r=7d959776-2dcc-4eb2-b0ad-3080f6bcdfa1&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWxfdGhlbWF0aWM&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyRk9MMVk3STI1UTJaJmVuY3J5cHRlZElkPUEwMDM3MjU5M09JT1VVQ1RPSjc5OCZlbmNyeXB0ZWRBZElkPUEzUkY4S1ZYVVRRUU1KJndpZGdldE5hbWU9c3BfZGV0YWlsX3RoZW1hdGljJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="
    ]

    text = amazon_page(urls[0])
    soup = BeautifulSoup(text, features='html.parser')
    title = soup.find(id='productTitle')
    price = soup.find(class_='a-price-whole')
    print(title.text)
    print(price.text)
    