import interface
import time


def user_scenario(driver):
    interface.log.info("simulation user scenario is started")

    interface.go_to_homepage(driver)  # go to home page
    interface.wait_banner(driver)  # close banner if it is displayed
    interface.click_to_nifty_bank(driver)  # choose graph "NIFTY BANK"
    time.sleep(1)
    interface.scroll_to_graph(driver)  # scroll to graph
    time.sleep(1)
    interface.click_to_view_all(driver)  # click to View All
    time.sleep(1)
    interface.choose_in_selector(driver)  # choose in selector "NIFTY ALPHA 50"
    interface.scroll_down(driver)  # scroll down
    time.sleep(1)
    interface.log.info("simulation user scenario is finished")
