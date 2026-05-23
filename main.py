import time

import routes
import self
from pip._internal import self_outdated_check

import pages
from pages import UrbanRoutesPage
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import data
import helpers


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver.implicitly_wait(5)

        if helpers.is_url_reachable (data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução")

    def test_set_route (self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert routes_page.get_from_location_volue() == data.ADDRESS_FROM
        assert routes_page.get_from_location_volue() == data.ADDRESS_TO
        time.sleep(10)



    def test_select_plan(self):
     self.driver.get(data.URBAN_ROUTES_URL)
    routes_page = UrbanRoutesPage(self.driver)
    routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
    routes_page.click_taxi_option()
    routes_page.click_comfort_icon
    assert routes_page.click_comfort_active()

    def test_fill_phone_number (self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_pages = UrbanRoutesPage(self.driver)
        routes_pages.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_pages.click_taxi_option()
        routes_pages.click_comfort_icon()
        routes_pages.click_number_text(data.PHONE_NUMBER)
        assert data.PHONE_NUMBER in routes_pages.numero_confirmado()



    def test_fill_card (self):
       self.driver.get(data.URBAN_ROUTES_URL)
       routes_pages = UrbanRoutesPage(self.driver)
       routes_pages.enter_location(data.ADDRESS_FROM, data.ADDRESS_TO)
       routes_pages.click_taxi_option()
       routes_pages.click_comfort_icon()
       routes_pages.click_payment_method()
       routes_pages.fill_card_data(data.CARD_NUMBER, data.CARD_CODE)
       assert data.CARD_CODE in routes_pages.numero_confirmado()


    def test_comment_foroutes_page (self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_pages = UrbanRoutesPage(self.driver)
        routes_pages.enter_location(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_pages.click_taxi_option()
        routes_pages.click_comfort_icon()
        routes_pages.fill_comment(data.COMMENT)
        assert data.COMMENT in routes-pages.comment_confirmed()




    def test_order_2_ice_creams (self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM,data.ADDRESS_TO)
        routes_page.click_taxi_option()
        routes_page.click_comfort_icon()
        routes_page.add_ice_cream()
        routes_page.add_ice_cream()
    assert routes_page.ice_cream_counter() == "2"





    @classmethod
    def teardown_class(cls):
        cls.driver.quit()