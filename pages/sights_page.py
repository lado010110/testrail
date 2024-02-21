from selenium.webdriver.common.by import By

from elements.button import Button
from pages.base_form import BaseForm


class SightsPage(BaseForm):
    __choose_ur_experience_txt = Button(By.XPATH, "//a[contains(text(),'აღმოაჩინე შენი თავგადასავალი')]",
                                        "ჩუს იურ ექსპერიანსზე გადასვლა")

    __chat = Button(By.XPATH, "//button[@aria-label='chat']", "ჩატის ღილაკზე დაკლიკება")

    def __init__(self):
        super().__init__(By.XPATH, "//a[contains(text(),'აღმოაჩინე შენი თავგადასავალი')]",
                         "სანახაობების გვერდზე შესვლა")

    def click_choose_ur_experience(self):
        self.__choose_ur_experience_txt.click()

    def click_to_chat(self):
        self.__chat.click()
