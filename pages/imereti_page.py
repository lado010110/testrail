from selenium.webdriver.common.by import By

from elements.button import Button
from elements.element import Element
from pages.base_form import BaseForm


class ImeretiPage(BaseForm):
    __map = Element(By.XPATH, "//div[@class='InterestsMapCore_InterestsMapCore__IREcV']", "იმერეთის რუკა")
    __map_screenshot = Element(By.XPATH, "//div[@class='InterestsMapCore_InterestsMapCore__IREcV']", "რუკა სქრინშოთი")
    __more_toggle_places = Button(By.XPATH, "//button[@data-test='map_toggle-0']", "მდებარეობის მენიუ")
    __more_toggle_imereti = Button(By.XPATH, "//button[@data-test='map-toggle-იმერეთი-2']", "იმერეთის მენიუ")
    __sairme = Button(By.XPATH, "//label[contains(text(),'საირმე')]", "საირმეს მონიშვნა")
    __more_toggle_sights = Button(By.XPATH, "//button[@data-test='map_toggle-1']", "სანახაობების მენიუ")
    __more_toggle_statue = Button(By.XPATH, "//button[@data-test='map-toggle-კულტურულიძეგლები-0']",
                                  "კულტურული ძეგელების მენიუ")
    __castle = Button(By.XPATH, "//label[contains(text(),'ციხესიმაგრეები')]", "ციხესიმაგრები")
    __move_to_airports = Element(By.XPATH, "//label[@data-test='map_checkbox-1']", "აეროპორტის ელემენტი")
    __airports = Button(By.XPATH, "//input[@data-test='map_checkbox-1']", "აეროპორტის ჩექბოქსი")
    __tourist_office = Button(By.XPATH, "//input[@data-test='map_checkbox-2']", "ტურისტული ოფისების ჩექბოქსი")

    def __init__(self):
        super().__init__(By.XPATH, "//div[@class='InterestsMapCore_InterestsMapCore__IREcV']",
                         "იმერეთის გვერდზე შესვლა")

    def move_to_map(self):
        self.__map.move_to_element()

    def screenshot_map(self):
        self.__map_screenshot.screenshot()

    def click_more_toggle_places(self):
        self.__more_toggle_places.click()

    def click_more_toggle_imereti(self):
        self.__more_toggle_imereti.click()

    def click_sairme(self):
        self.__sairme.click()

    def click_more_toggle_sights(self):
        self.__more_toggle_sights.click()

    def click_more_toggle_statue(self):
        self.__more_toggle_statue.click()

    def click_castle(self):
        self.__castle.click()

    def move_to_element(self):
        self.__move_to_airports.move_to_element()

    def click_airports(self):
        self.__airports.click()

    def click_tourist(self):
        self.__tourist_office.click()
