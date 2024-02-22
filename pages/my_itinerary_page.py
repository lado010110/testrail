from selenium.webdriver.common.by import By

from elements.button import Button
from pages.base_form import BaseForm
from utils.DriverUtils import DriverUtils


class MyItineraryPage(BaseForm):
    __activ = Button(By.XPATH, "//a[@data-test='4-დღიანი ჯიპ-ტური: სამცხე ჯავახეთი - აჭარა']", "აჭარა აქტივობა")
    __place_tbilisi = Button(By.XPATH, "//a[@data-test='თბილისი']", "თბილისი")
    __tur = Button(By.XPATH, "//a[@data-test='ორდღიანი ტური სვანეთში']", "ტური სვანეთი")
    __sort_activ_menu = Button(By.XPATH, "//button[contains(text(),'აქტივობა')]", "აქტივობის სორტი")
    __sort_place_menu = Button(By.XPATH, "//button[contains(text(),'ადგილმდებარეობები')]", "ადგილმდებარეობების სორტი")
    __sort_tur_menu = Button(By.XPATH, "//button[contains(text(),'ტურები')]", "ტურები სორტი")

    def __init__(self):
        super().__init__(By.XPATH, "//div[@class='FavoritesPage_FavoritesPage__Title__VXFLQ']",
                         "ფავორიტების გვერდზე შესვლა")

    def click_activ(self):
        locator = By.XPATH, self.__activ.locator
        DriverUtils.wait_for_clickable(locator)
        self.__activ.click()

    def click_tbilisi(self):
        locator = By.XPATH, self.__place_tbilisi.locator
        DriverUtils.wait_for_clickable(locator)
        self.__place_tbilisi.click()

    def click_tur(self):
        locator = By.XPATH, self.__tur.locator
        DriverUtils.wait_for_clickable(locator)
        self.__tur.click()

    def click_sort_menu_activ(self):
        locator = By.XPATH, self.__sort_activ_menu.locator
        DriverUtils.wait_for_clickable(locator)
        self.__sort_activ_menu.click()

    def click_sort_menu_places(self):
        locator = By.XPATH, self.__sort_place_menu.locator
        DriverUtils.wait_for_clickable(locator)
        self.__sort_place_menu.click()

    def click_sort_menu_tur(self):
        locator = By.XPATH, self.__sort_tur_menu.locator
        DriverUtils.wait_for_clickable(locator)
        self.__sort_tur_menu.click()
