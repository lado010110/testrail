from selenium.webdriver.common.by import By

from elements.button import Button
from pages.base_form import BaseForm
from utils.DriverUtils import DriverUtils


class WhyGeorgiaPage(BaseForm):
    __menu_why_georgia = Button(By.XPATH, "//a[@data-test='header-menu-რატომსაქართველო']", "რატომ საქართველოს მენიუ")
    __main_cities = Button(By.XPATH, "//div[@class='why_georgia_geography_swiper_next']", "მთავარი ქალაქების სექცია")
    __main_cities_batumi = Button(By.XPATH, "//div[@class='why_georgia_marker adjara_marker']", "ბათუმი")
    __main_cities_qutaisi = Button(By.XPATH, "//div[@class='why_georgia_marker imereti_marker']", "ქუთაისი")
    __main_cities_tbilisi = Button(By.XPATH, "//div[@class='why_georgia_marker tbilisi_marker']", "თბილისი")
    __main_cities_learn_more = Button(By.XPATH,
                                      "//div[@class='why_georgia_geography_wrapper']//a[@class='custom white']",
                                      "გაიგე მეტი ქალაქები")
    __winter = Button(By.XPATH, "//span[contains(text(),'ზამთარი')]", "ზამთარი")
    __spring = Button(By.XPATH, "//span[contains(text(),'გაზაფხული')]", "გაზაფხული")
    __fall = Button(By.XPATH, "//span[contains(text(),'შემოდგომა')]", "შემოდგომა")
    __summer = Button(By.XPATH, "//span[contains(text(),'ზაფხული')]", "ზაფხული")
    __season_learn_more = Button(By.XPATH, "//div[@class='slide active']//strong[contains(text(),'გაიგე მეტი')]",
                                 "გაიგე მეტი სეზონები")
    __wine_learn_more = Button(By.XPATH,
                               "//div[@class='cradle_of_wine_top_col']//strong[contains(text(),'გაიგე მეტი')]",
                               "გაიგე მეტი ღვინო")
    __alphabet_learn_more = Button(By.XPATH,
                                   "//section[@class='unique_alphabet']//strong[contains(text(),'გაიგე მეტი')]",
                                   "გაიგე მეტი დამწერლობა")
    __kitchen_learn_more = Button(By.XPATH, "//div[@class='why_georiga_info_box_cuisine']//a[@class='custom white']",
                                  "გაიგე მეტი სამზარეულო")
    __music_learn_more = Button(By.XPATH,
                                "//div[@class='unique_folklore_inner']//strong[contains(text(),'გაიგე მეტი')]",
                                "გაიგე მეტი ფოლკლორი")
    __dance_learn_more = Button(By.XPATH,
                                "//div[@class='language_of_dance_container']//strong[contains(text(),'გაიგე მეტი')]",
                                "გაიგე მეტი ცეკვა")
    __how_is_georgia = Button(By.XPATH, "//h4[contains(text(),'ნახე, როგორია საქართველო')]", "როგორია საქართველო")
    __history_learn_more = Button(By.XPATH,
                                  "//div[@class='culture_history_col']//strong[contains(text(),'გაიგე მეტი')]",
                                  "გაიგე მეტი ისტორია")
    __civilisation_learn_more = Button(By.XPATH, "//div[@class='first_european_col']//a[@class='custom white']",
                                       "გაიგე მეტი ცივილიზაცია")
    __highest_learn_more = Button(By.XPATH, "//div[@class='highest_settlement_col']//a[@class='custom white']",
                                  "გაიგე მეტი მაღალი დასახლება")
    __travel_to_georgia = Button(By.XPATH, "//div[@class='why_subscribe_wrapper']//a[@class='custom white']",
                                 "იმოგზაურე საქართველოში")
    __left_bar_1 = Button(By.XPATH, "//span[@data-test='screen_1']", "სექცია 1")
    __left_bar_2 = Button(By.XPATH, "//span[@data-test='screen_2']", "სექცია 2")
    __left_bar_3 = Button(By.XPATH, "//span[@data-test='screen_3']", "სექცია 3")
    __left_bar_4 = Button(By.XPATH, "//span[@data-test='screen_4']", "სექცია 4")
    __left_bar_5 = Button(By.XPATH, "//span[@data-test='screen_5']", "სექცია 5")
    __left_bar_6 = Button(By.XPATH, "//span[@data-test='screen_6']", "სექცია 6")
    __left_bar_7 = Button(By.XPATH, "//span[@data-test='screen_7']", "სექცია 7")
    __left_bar_8 = Button(By.XPATH, "//span[@data-test='screen_8']", "სექცია 8")
    __left_bar_9 = Button(By.XPATH, "//span[@data-test='screen_9']", "სექცია 9")
    __left_bar_10 = Button(By.XPATH, "//span[@data-test='screen_10']", "სექცია 10")
    __left_bar_11 = Button(By.XPATH, "//span[@data-test='screen_11']", "სექცია 11")
    __left_bar_12 = Button(By.XPATH, "//span[@data-test='screen_12']", "სექცია 12")

    def __init__(self):
        super().__init__(By.XPATH, "//div[@class='why_georgia_hero_content']",
                         "რატომ საქართველოზე შესვლა")

    def click_why_georgia(self):
        locator = By.XPATH, self.__menu_why_georgia.locator
        DriverUtils.wait_for_clickable(locator)
        self.__menu_why_georgia.click()

    def click_main_cities(self):
        locator = By.XPATH, self.__main_cities.locator
        DriverUtils.wait_for_clickable(locator)
        self.__main_cities.click()

    def click_batumi(self):
        locator = By.XPATH, self.__main_cities_batumi.locator
        DriverUtils.wait_for_clickable(locator)
        self.__main_cities_batumi.click()

    def click_qutaisi(self):
        locator = By.XPATH, self.__main_cities_qutaisi.locator
        DriverUtils.wait_for_clickable(locator)
        self.__main_cities_qutaisi.click()

    def click_tbilisi(self):
        locator = By.XPATH, self.__main_cities_tbilisi.locator
        DriverUtils.wait_for_clickable(locator)
        self.__main_cities_tbilisi.click()

    def click_main_cities_learn_more(self):
        locator = By.XPATH, self.__main_cities_learn_more.locator
        DriverUtils.wait_for_clickable(locator)
        self.__main_cities_learn_more.click()

    def click_winter(self):
        locator = By.XPATH, self.__winter.locator
        DriverUtils.wait_for_clickable(locator)
        self.__winter.click()

    def click_summer(self):
        locator = By.XPATH, self.__summer.locator
        DriverUtils.wait_for_clickable(locator)
        self.__summer.click()

    def click_fall(self):
        locator = By.XPATH, self.__fall.locator
        DriverUtils.wait_for_clickable(locator)
        self.__fall.click()

    def click_spring(self):
        locator = By.XPATH, self.__spring.locator
        DriverUtils.wait_for_clickable(locator)
        self.__spring.click()

    def click_season_learn_more(self):
        locator = By.XPATH, self.__season_learn_more.locator
        DriverUtils.wait_for_clickable(locator)
        self.__season_learn_more.click()

    def click_wine_learn_more(self):
        locator = By.XPATH, self.__wine_learn_more.locator
        DriverUtils.wait_for_clickable(locator)
        self.__wine_learn_more.click()

    def click_alphabet_learn_more(self):
        locator = By.XPATH, self.__alphabet_learn_more.locator
        DriverUtils.wait_for_clickable(locator)
        self.__alphabet_learn_more.click()

    def click_kitchen_learn_more(self):
        locator = By.XPATH, self.__kitchen_learn_more.locator
        DriverUtils.wait_for_clickable(locator)
        self.__kitchen_learn_more.click()

    def click_music_learn_more(self):
        locator = By.XPATH, self.__music_learn_more.locator
        DriverUtils.wait_for_clickable(locator)
        self.__music_learn_more.click()

    def click_dance_learn_more(self):
        locator = By.XPATH, self.__dance_learn_more.locator
        DriverUtils.wait_for_clickable(locator)
        self.__dance_learn_more.click()

    def click_how_is_georgia(self):
        locator = By.XPATH, self.__how_is_georgia.locator
        DriverUtils.wait_for_clickable(locator)
        self.__how_is_georgia.click()

    def click_history_learn_more(self):
        locator = By.XPATH, self.__history_learn_more.locator
        DriverUtils.wait_for_clickable(locator)
        self.__history_learn_more.click()

    def click_civilisation_learn_more(self):
        locator = By.XPATH, self.__civilisation_learn_more.locator
        DriverUtils.wait_for_clickable(locator)
        self.__civilisation_learn_more.click()

    def click_highest_learn_more(self):
        locator = By.XPATH, self.__highest_learn_more.locator
        DriverUtils.wait_for_clickable(locator)
        self.__highest_learn_more.click()

    def click_travel_to_georgia(self):
        locator = By.XPATH, self.__travel_to_georgia.locator
        DriverUtils.wait_for_clickable(locator)
        self.__travel_to_georgia.click()

    def click_left_bar_1(self):
        locator = By.XPATH, self.__left_bar_1.locator
        DriverUtils.wait_for_clickable(locator)
        self.__left_bar_1.click()

    def click_left_bar_2(self):
        locator = By.XPATH, self.__left_bar_2.locator
        DriverUtils.wait_for_clickable(locator)
        self.__left_bar_2.click()

    def click_left_bar_3(self):
        locator = By.XPATH, self.__left_bar_3.locator
        DriverUtils.wait_for_clickable(locator)
        self.__left_bar_3.click()

    def click_left_bar_4(self):
        locator = By.XPATH, self.__left_bar_4.locator
        DriverUtils.wait_for_clickable(locator)
        self.__left_bar_4.click()

    def click_left_bar_5(self):
        locator = By.XPATH, self.__left_bar_5.locator
        DriverUtils.wait_for_clickable(locator)
        self.__left_bar_5.click()

    def click_left_bar_6(self):
        locator = By.XPATH, self.__left_bar_6.locator
        DriverUtils.wait_for_clickable(locator)
        self.__left_bar_6.click()

    def click_left_bar_7(self):
        locator = By.XPATH, self.__left_bar_7.locator
        DriverUtils.wait_for_clickable(locator)
        self.__left_bar_7.click()

    def click_left_bar_8(self):
        locator = By.XPATH, self.__left_bar_8.locator
        DriverUtils.wait_for_clickable(locator)
        self.__left_bar_8.click()

    def click_left_bar_9(self):
        locator = By.XPATH, self.__left_bar_9.locator
        DriverUtils.wait_for_clickable(locator)
        self.__left_bar_9.click()

    def click_left_bar_10(self):
        locator = By.XPATH, self.__left_bar_10.locator
        DriverUtils.wait_for_clickable(locator)
        self.__left_bar_10.click()

    def click_left_bar_11(self):
        locator = By.XPATH, self.__left_bar_11.locator
        DriverUtils.wait_for_clickable(locator)
        self.__left_bar_11.click()

    def click_left_bar_12(self):
        locator = By.XPATH, self.__left_bar_12.locator
        DriverUtils.wait_for_clickable(locator)
        self.__left_bar_12.click()
