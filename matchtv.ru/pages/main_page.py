from .base_page import BasePage
# from selenium.webdriver.common.by import By
from .locators import MainPageLocators

class MainPage(BasePage):
    def should_be_part_of_header(self):
        assert self.is_element_present(*MainPageLocators.LOGO_PIC), "LOGO_PIC not found"
        assert self.is_element_present(*MainPageLocators.ON_AIR), "ON_AIR not found"
        assert self.is_element_present(*MainPageLocators.TOKYO_2020), "TOKYO_2020 not found"
        assert self.is_element_present(*MainPageLocators.TVGUIDE), "TVGUIDE not found"
        assert self.is_element_present(*MainPageLocators.LIVE), "LIVE not found"
        assert self.is_element_present(*MainPageLocators.NEWS), "NEWS not found"
        assert self.is_element_present(*MainPageLocators.MATCHPREMIER), "MATCHPREMIER not found"
        assert self.is_element_present(*MainPageLocators.VIDEO), "VIDEO not found"
        assert self.is_element_present(*MainPageLocators.SUBSCRIPTIONS), "SUBSCRIPTIONS not found"
        assert self.is_element_present(*MainPageLocators.MATCH_APP), "MATCH_APP not found"
        assert self.is_element_present(*MainPageLocators.CHANNEL_STRANA), "CHANNEL_STRANA not found"

    def should_be_types_of_sports(self):
        assert self.is_element_present(*MainPageLocators.FOOTBALL), "FOOTBALL not found"
        assert self.is_element_present(*MainPageLocators.HOCKEY), "HOCKEY not found"
        assert self.is_element_present(*MainPageLocators.BOXING), "BOXING not found"
        assert self.is_element_present(*MainPageLocators.BASKETBALL), "BASKETBALL not found"
        assert self.is_element_present(*MainPageLocators.FORMULA_1), "FORMULA_1 not found"
        assert self.is_element_present(*MainPageLocators.FIGURE_SKATING), "FIGURE_SKATING not found"
        assert self.is_element_present(*MainPageLocators.BIATHLON), "BIATHLON not found"
        assert self.is_element_present(*MainPageLocators.SKIING), "SKIING not found"
        assert self.is_element_present(*MainPageLocators.KORONAVIRUS), "KORONAVIRUS not found"
        assert self.is_element_present(*MainPageLocators.CYBER), "CYBER not found"
        assert self.is_element_present(*MainPageLocators.SUMMER), "SUMMER not found"
        assert self.is_element_present(*MainPageLocators.WINTER), "WINTER not found"
        assert self.is_element_present(*MainPageLocators.AUTOSPORT), "AUTOSPORT not found"
        assert self.is_element_present(*MainPageLocators.ATHLETICS), "ATHLETICS not found"
        assert self.is_element_present(*MainPageLocators.VOLLEYBALL), "VOLLEYBALL not found"
        assert self.is_element_present(*MainPageLocators.CHESS), "CHESS not found"
        assert self.is_element_present(*MainPageLocators.TENNIS), "TENNIS not found"
        assert self.is_element_present(*MainPageLocators.ATHLETES), "ATHLETES not found"
        assert self.is_element_present(*MainPageLocators.TOURS_3D), "TOURS_3D not found"
        assert self.is_element_present(*MainPageLocators.N_AIR), "N_AIR not found"
