from selenium.webdriver.common.by import By
from selenium.webdriver.support import expect_conditions as ec
from selenium.webdriver.support.wait import webdriverWait
import time

class UrbanRoutesPage:
    # Seção DE e PARA
from_field = (By.ID, 'from')
to_field = (By.ID, 'to')

def __init__(self,driver):
    sel.driver = driver

    def enter_from_location(self, from_text):
        self.driver.find_element(*self.from_field).send_keys(from_text)

    def enter_from_location(self, to_text):
        self.driver.find_element(*self.to_field).send_keys(to_text)

    def enter_locations(self, from_text, to_text):
        self.enter_from_location(from_text)
        self.enter_to_locations(to_text)
    def get_to_location_value(self):
        return WebDriverWait(self.driver, timeout: 3).until(
            EC.visibility_of_element_located(self.to_field)
        ).get_attribute('value')
        _
