from curses import termattrs
import booking.constants as const
from selenium import webdriver
from selenium.webdriver.common.by import By

class Booking(webdriver.Chrome):
    def __init__(self, driver_path="/usr/local/bin/chromedriver", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        # to use all function from webdriver.Chrome
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        # self.maximize_window()

    # to test and exit automatically 
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)
    
    def change_currency(self, currency=None):
        currency_element = self.find_element(By.CSS_SELECTOR, 'button[data-tooltip-text="Choose your currency"]')
        currency_element.click()
        selected_currency_element = self.find_element(By.CSS_SELECTOR, f'a[data-modal-header-async-url-param*="selected_currency={currency}"]')
        selected_currency_element.click()

        