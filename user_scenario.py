from selenium.webdriver.common.by import By
import interface
import time


def user_scenario(driver):
    driver.find_element(By.CSS_SELECTOR, '#link_0').click()  # go to home page
    interface.wait_banner(driver)  # close banner if it is displayed
    driver.find_element(By.CSS_SELECTOR, "#NIFTY\ BANK").click()  # choose graph "NIFTY BANK"
    time.sleep(1)

    # scroll to graph
    element = driver.find_element(By.LINK_TEXT, "View All")
    interface.scroll_to_element(driver, element)
    driver.execute_script("window.scrollBy(0, 250);")  # additionally scroll down to see the button

    time.sleep(1)
    element.click()

    time.sleep(1)
    interface.input_selector(driver)  # choose in selector "NIFTY ALPHA 50"

    # scroll down
    time.sleep(1)
    element = driver.find_element(By.CSS_SELECTOR, "#marketWatchEquityCmsNote")
    interface.scroll_to_element(driver, element)
    time.sleep(3)
