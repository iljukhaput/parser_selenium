from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time
from selenium_stealth import stealth


start_page = 'https://www.nseindia.com/'


def init_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )
    return driver


def input_selector(driver):
    element = driver.find_element(By.ID, 'equitieStockSelect')
    selector = Select(element)
    selector.select_by_visible_text('NIFTY ALPHA 50')


def scroll_to_element(driver, element):
    actions = ActionChains(driver)
    actions.scroll_to_element(element)
    actions.perform()


def wait_banner(driver):
    time.sleep(3)
    waiting_time = 3
    wait = WebDriverWait(driver, waiting_time)
    try:
        element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="myModal"]/div/div')))
        close_btn = element.find_element(By.CLASS_NAME, 'close')
        close_btn.click()
        time.sleep(3)
    except Exception:
        pass


def hover_to_element(driver):
    hover = driver.find_element(By.ID, 'link_2')
    actions = ActionChains(driver)
    actions.move_to_element(hover)
    actions.perform()
