from selenium.webdriver.common.by import By
import parser
import user_scenario
import interface


def test_task():
    driver = interface.init_driver()
    driver.get(interface.start_page)
    interface.wait_banner(driver)  # close banner if it is displayed
    interface.hover_to_element(driver)  # hover to MARKET DATA
    driver.find_element(By.LINK_TEXT, 'Pre-Open Market').click()

    parser.pars(driver)  # parsing to csv file

    user_scenario.user_scenario(driver)  # simulate a user scenario for using the site

    driver.quit()


def main():
    test_task()


if __name__ == main():
    main()
