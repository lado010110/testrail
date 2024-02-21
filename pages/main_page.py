from selenium.webdriver.common.by import By

from elements.button import Button
from elements.element import Element
from pages.base_form import BaseForm


class MainPage(BaseForm):
    __places = Button(By.XPATH, "//a[@data-test='header-menu-ადგილები']", "ადგილების მენიუზე კლიკი")
    __close_ri_line = Element(By.XPATH, "//button[@aria-label='Cookie პოლიტიკის შესახებ ფანჯრის დახურვა']",
                              "გათიშვა ქუქის")
    __sights = Button(By.XPATH,"//a[@data-test='header-menu-სანახაობები']", "სანახაობების მენიუზე კლიკი")

    def __init__(self):
        super().__init__(By.XPATH, "//a[@data-test='header-menu-მეტი']", "მთავარი გვერდზე შესვლა")

    def click_places_button(self):
        self.__places.click()

    def close_ri_line(self):
        self.__close_ri_line.click()

    def click_sights_menu(self):
        self.__sights.click()
