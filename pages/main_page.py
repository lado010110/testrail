from selenium.webdriver.common.by import By

from elements.button import Button
from elements.element import Element
from elements.input import Input
from pages.base_form import BaseForm
from utils.DriverUtils import DriverUtils


class MainPage(BaseForm):
    __places = Button(By.XPATH, "//a[@data-test='header-menu-ადგილები']", "ადგილების მენიუზე კლიკი")
    __close_ri_line = Element(By.XPATH, "//button[@aria-label='Cookie პოლიტიკის შესახებ ფანჯრის დახურვა']",
                              "გათიშვა ქუქის")
    __sights = Button(By.XPATH, "//a[@data-test='header-menu-სანახაობები']", "სანახაობების მენიუზე კლიკი")
    __header_map = Button(By.XPATH, "//a[@data-test='header-map']", "მაპის იკონი მთავარ გვერდზე")
    __fill_search = Input(By.XPATH, "//input[@data-test='header-search']", "სერჩი ინფუთი")
    __header_search = Button(By.XPATH, "//em[@class='ri-search-line']", "სერჩის ღილაკი")
    __header_favorites = Button(By.XPATH, "//a[@data-test='header-favorites']", "ფავორიტები")

    def __init__(self):
        super().__init__(By.XPATH, "//a[@data-test='header-menu-მეტი']", "მთავარი გვერდზე შესვლა")

    def click_places_button(self):
        locator = By.XPATH, self.__places.locator
        DriverUtils.wait_for_clickable(locator)
        self.__places.click()

    def close_ri_line(self):
        locator = By.XPATH, self.__close_ri_line.locator
        DriverUtils.wait_for_clickable(locator)
        self.__close_ri_line.click()

    def click_sights_menu(self):
        locator = By.XPATH, self.__sights.locator
        DriverUtils.wait_for_clickable(locator)
        self.__sights.click()

    def click_map_menu(self):
        locator = By.XPATH, self.__header_map.locator
        DriverUtils.wait_for_clickable(locator)
        self.__header_map.click()

    def click_search(self):
        locator = By.XPATH, self.__header_search.locator
        DriverUtils.wait_for_clickable(locator)
        self.__header_search.click()

    def fill_search_menu_sight(self, sight_name):
        locator = By.XPATH, self.__fill_search.locator
        DriverUtils.wait_for_clickable(locator)
        self.__fill_search.send_text(sight_name)

    def fill_search_menu_tur(self, tur_name):
        locator = By.XPATH, self.__fill_search.locator
        DriverUtils.wait_for_clickable(locator)
        self.__fill_search.send_text(tur_name)

    def fill_search_menu_place(self, place_name):
        locator = By.XPATH, self.__fill_search.locator
        DriverUtils.wait_for_clickable(locator)
        self.__fill_search.send_text(place_name)

    def fill_search_menu_activiti(self, activ_name):
        locator = By.XPATH, self.__fill_search.locator
        DriverUtils.wait_for_clickable(locator)
        self.__fill_search.send_text(activ_name)

    def click_favorites_menu(self):
        locator = By.XPATH, self.__header_favorites.locator
        DriverUtils.wait_for_clickable(locator)
        self.__header_favorites.click()
