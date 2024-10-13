from flask import Flask
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from bs4 import BeautifulSoup
import os

app = Flask(__name__)

@app.route('/')
def index():
    options = ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)

    driver.get("https://www.maxmilhas.com.br/vender-milhas")

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    driver.implicitly_wait(10)

    prices = [element.get_text() for element in soup.select('.fidelities-slider_card_price')]
    programs = [element.get_text() for element in soup.select('.fidelities-slider_card_names')]

    quotation = dict(zip(programs, prices))
    driver.quit()
    return str(quotation)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
