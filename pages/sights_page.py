from selenium.webdriver.common.by import By

from elements.button import Button
from pages.base_form import BaseForm
from utils.DriverUtils import DriverUtils


class SightsPage(BaseForm):
    __choose_ur_experience_txt = Button(By.XPATH, "//a[contains(text(),'აღმოაჩინე შენი თავგადასავალი')]",
                                        "ჩუს იურ ექსპერიანსზე გადასვლა")

    __chat = Button(By.XPATH, "//button[@aria-label='chat']", "ჩატის ღილაკზე დაკლიკება")
    __canyon_button = Button(By.XPATH, "//a[@data-test='card-ოკაცესკანიონი']", "ოკაცეს კანიონი")
    __hart_button = Button(By.XPATH, "//button[@class='favourite-large small white']", "დამატება ფავორიტებში")
    __tur_hart_button = Button(By.XPATH, "//button[@class='favourite-large small']", "ტურის დამატება ფავორიტებში")

    def __init__(self):
        super().__init__(By.XPATH, "//a[contains(text(),'აღმოაჩინე შენი თავგადასავალი')]",
                         "სანახაობების გვერდზე შესვლა")

    def click_choose_ur_experience(self):
        self.__choose_ur_experience_txt.click()

    def click_to_chat(self):
        self.__chat.click()

    def click_hart_button(self):
        locator = By.XPATH, self.__hart_button.locator
        DriverUtils.wait_for_clickable(locator)
        self.__hart_button.click()

    def click_tur_hart_button(self):
        locator = By.XPATH, self.__tur_hart_button.locator
        DriverUtils.wait_for_clickable(locator)
        self.__tur_hart_button.click()
