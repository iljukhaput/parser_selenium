import sys
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_data(driver):
    bs = BeautifulSoup(driver.page_source, 'html.parser')
    rows = bs.find_all('tr')
    tablelist = []

    if len(rows) == 0:
        return tablelist

    for row in rows:
        name = row.find('a', attrs={'class': 'symbol-word-break'})
        price = row.find('td', attrs={'class': 'bold text-right'})
        if name is not None and price is not None:
            line = {
                'name': name.text,
                'price': price.text
            }
            tablelist.append(line)

    return tablelist


def write_data(data, file_name):
    if len(data) != 0:
        df = pd.DataFrame(data)
        df.to_csv(file_name)
        return True
    else:
        return False


def pars(driver):
    waiting_time = 5
    wait = WebDriverWait(driver, waiting_time)
    table = wait.until(EC.presence_of_element_located((By.ID, 'livePreTable')))
    if not table.is_displayed():
        print(driver.page_source + ": the table was not displayed")
        sys.exit(1)

    data = get_data(driver)
    file_name = 'final_prices.csv'
    write_data_done = write_data(data, file_name)
    if not write_data_done:
        print(driver.page_source + ": there is no data from the table")
        sys.exit(1)
