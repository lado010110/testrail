from selenium.webdriver.common.by import By

from elements.button import Button
from elements.input import Input
from pages.base_form import BaseForm
from utils.DriverUtils import DriverUtils


class SearchPage(BaseForm):
    __search_input = Input(By.XPATH, "//div[@class='SearchPageSidebar_SearchPageSidebar__Title__avzsz']",
                           "სერჩის ინფუთი")
    __sort_pages_menu = Button(By.XPATH, "//button[contains(text(),'გვერდები')]", "გვერდები")

    __sight_canyon = Button(By.XPATH, "//a[@data-test='ოკაცეს კანიონი']", "ოკაცეს კანიონი")
    __sort_tur_menu = Button(By.XPATH, "//button[contains(text(),'ტურისტული გეგმები')]", "ტურისტული გეგმა")

    def __init__(self):
        super().__init__(By.XPATH, "//div[@class='SearchPageSidebar_SearchPageSidebar__Title__avzsz']",
                         "სერჩის გვერდზე შესვლა")

    def click_sight_canyon(self):
        locator = By.XPATH, self.__sight_canyon.locator
        DriverUtils.wait_for_clickable(locator)
        self.__sight_canyon.click()

    def click_sort_pages(self):
        locator = By.XPATH, self.__sort_pages_menu.locator
        DriverUtils.wait_for_clickable(locator)
        self.__sort_pages_menu.click()

    def click_sort_tur_menu(self):
        locator = By.XPATH, self.__sort_tur_menu.locator
        DriverUtils.wait_for_clickable(locator)
        self.__sort_tur_menu.click()
