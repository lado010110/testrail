from selenium.webdriver.common.by import By

from elements.button import Button
from pages.base_form import BaseForm
from utils.DriverUtils import DriverUtils


class PlacesPage(BaseForm):
    __imereti_element = Button(By.XPATH, "//strong[contains(text(),'იმერეთი')]", "იმერეთზე დაკლიკება")
    __imereti = Button(By.XPATH,
                       "//div[@class='categories_col']//a[contains(text(),'იმერეთი')]",
                       "იმერეთზე დაკლიკება")

    def __init__(self):
        super().__init__(By.XPATH, "//h1[contains(text(),'ადგილმდებარეობები საქართველოში')]",
                         "ადგილების გვერდზე შესვლა")

    def scroll_down_to_imereti(self):
        locator = By.XPATH, self.__imereti_element.locator
        DriverUtils.wait_for_clickable(locator)
        self.__imereti_element.move_to_element()

    def click_imereti(self):
        locator = By.XPATH, self.__imereti.locator
        DriverUtils.wait_for_clickable(locator)
        self.__imereti.click()
