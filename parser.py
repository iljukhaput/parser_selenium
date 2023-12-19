import sys
import time
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import interface


def get_data(driver):
    bs = BeautifulSoup(driver.page_source, 'html.parser')
    rows = bs.find_all('tr')
    tablelist = []

    if len(rows) == 0:
        interface.log.error("data was not received")
        sys.exit(1)

    for row in rows:
        name = row.find('a', attrs={'class': 'symbol-word-break'})
        price = row.find('td', attrs={'class': 'bold text-right'})
        if name is not None and price is not None:
            line = {
                'name': name.text,
                'price': price.text
            }
            tablelist.append(line)

    interface.log.info("data was received")
    return tablelist


def write_data(data, file_name):
    try:
        df = pd.DataFrame(data)
        df.to_csv(file_name)
        interface.log.info("data was recorded to the file")
    except Exception:
        interface.log.error("data was not recorded to the file")
        sys.exit(1)


def pars(driver):
    interface.log.info("parsing is started")
    waiting_time = 5
    wait = WebDriverWait(driver, waiting_time)
    table = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#livePreTable')))
    time.sleep(2)
    if not table.is_displayed():
        interface.log.error("the table was not displayed")
        sys.exit(1)

    data = get_data(driver)
    file_name = 'final_prices.csv'
    write_data(data, file_name)
