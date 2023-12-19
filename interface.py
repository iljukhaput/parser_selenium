from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time
from selenium_stealth import stealth
import logging
import sys


logging.basicConfig(filename='log.txt',
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S'
                    )
log = logging.getLogger()


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
    log.info('driver initialized')
    return driver


def input_selector(driver):
    element = driver.find_element(By.CSS_SELECTOR, '#equitieStockSelect')
    selector = Select(element)
    selector.select_by_visible_text('NIFTY ALPHA 50')


def scroll_to_element(driver, element):
    try:
        actions = ActionChains(driver)
        actions.scroll_to_element(element)
        actions.perform()
        log.info('scroll to element - done')
    except Exception:
        log.error('scroll to element - failed')


def wait_banner(driver):
    log.info('waiting for banner')
    time.sleep(3)
    waiting_time = 3
    wait = WebDriverWait(driver, waiting_time)
    try:
        element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#myModal > div > div')))
        close_btn = element.find_element(By.CLASS_NAME, 'close')
        close_btn.click()
        time.sleep(3)
        log.info('banner was displayed and closed')
    except Exception:
        log.info('banner was not displayed')


def hover_to_element(driver):
    try:
        hover = driver.find_element(By.CSS_SELECTOR, '#link_2')
        actions = ActionChains(driver)
        actions.move_to_element(hover)
        actions.perform()
        log.info('hover to element - done')
    except Exception:
        log.error('hover to element - failed')
        sys.exit(1)


def click_pre_open_market(driver):
    try:
        driver.find_element(By.CSS_SELECTOR, '#main_navbar > ul > li:nth-child(3) > div > div.container > div > div:nth-child(1) > ul > li:nth-child(1) > a').click()
        log.info('click to Pre-Open Market done')
    except Exception:
        log.error('click to Pre-Open Market failed')
        sys.exit(1)


def go_to_homepage(driver):
    try:
        driver.find_element(By.CSS_SELECTOR, '#link_0').click()
        log.info("go to home page - done")
    except Exception:
        log.error("go to home page - failed")
        sys.exit(1)


def click_to_nifty_bank(driver):
    try:
        driver.find_element(By.CSS_SELECTOR, "#NIFTY\ BANK").click()
        log.info('choose graph "NIFTY BANK" - done')
    except Exception:
        log.error('choose graph "NIFTY BANK" - failed')
        sys.exit(1)


def scroll_to_graph(driver):
    try:
        element = driver.find_element(By.LINK_TEXT, "View All")
        scroll_to_element(driver, element)
        driver.execute_script("window.scrollBy(0, 250);")  # additionally scroll down to see the button
        log.info('scroll to graph - done')
    except Exception:
        log.error('scroll to graph - failed')
        sys.exit(1)


def click_to_view_all(driver):
    try:
        element = driver.find_element(By.LINK_TEXT, "View All")
        element.click()
        log.info('click to View All - done')
    except Exception:
        log.error('click to View All - failed')
        sys.exit(1)


def choose_in_selector(driver):
    try:
        input_selector(driver)
        log.info('choose in selector "NIFTY ALPHA 50" - done')
    except Exception:
        log.error('choose in selector "NIFTY ALPHA 50" - failed')
        sys.exit(1)


def scroll_down(driver):
    try:
        element = driver.find_element(By.CSS_SELECTOR, "#marketWatchEquityCmsNote")
        scroll_to_element(driver, element)
        log.info('scroll down - done')
    except Exception:
        log.error('scroll down - failed')
        sys.exit(1)
