from selenium.webdriver.common.by import By

from elements.button import Button
from elements.element import Element
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
    __batumi_visible = Element(By.XPATH, "//h1[contains(text(),'ბათუმი')]", "ბათუმის გვერდზე შესვლა")
    __qutaisi_visible = Element(By.XPATH, "//h1[contains(text(),'ქუთაისი')]", "ქუთაისის გვერდზე შესვლა")
    __tbilisi_visible = Element(By.XPATH, "//h1[contains(text(),'თბილისი')]", "თბილისის გვერდზე შესვლა")
    __geography_visible = Element(By.XPATH, "//h1[contains(text(),'საქართველოს გეოგრაფია')]",
                                  "საქართველოს გეოგრაფის გვერდზე შესვლა")
    __seasons_visible = Element(By.XPATH, "//h1[contains(text(),'სეზონურობა საქართველოში')]",
                                "სეზონურობის გვერდზე შესვლა")
    __wine_visible = Element(By.XPATH, "//h1[contains(text(),'საქართველო როგორც ღვინის აკვანი')]",
                             "ღვინის აკვანი გვერდზე შესვლა")
    __alphabet_visible = Element(By.XPATH, "//h1[contains(text(),'უნიკალური ქართული ანბანი')]",
                                 "ანბანის გვერდზე შესვლა")
    __kitchen_visible = Element(By.XPATH, "//h1[contains(text(),'უგემრიელესი ქართული სამზარეულო')]",
                                "სამზარეულოს გვერდზე შესვლა")
    __music_visible = Element(By.XPATH, "//h1[contains(text(),'უნიკალური ქართული ფოლკლორი')]",
                              "ფოლკლორის გვერდზე შესვლა")
    __dance_visible = Element(By.XPATH, "//h1[contains(text(),'ქართული ცეკვა')]", "ცეკვას გვერდზე შესვლა")
    __history_visible = Element(By.XPATH, "//h1[contains(text(),'საქართველოს ისტორია')]", "ისტორის გვერდზე შესვლა")
    __civilisation_visible = Element(By.XPATH, "//h1[contains(text(),'პირველი ევროპული ცივილიზაცია')]",
                                     "ცივილიზაცის გვერდზე შესვლა")
    __highest_visible = Element(By.XPATH, "//h1[contains(text(),'ევროპის ყველაზე მაღალი დასახლებული პუნქტი საქართვე')]",
                                "ევროპის ყველაზე მაღალი დასახლებული პუნქტის გვერდზე შესვლა")
    __travel_visible = Element(By.XPATH, "//h1[contains(text(),'აღმოაჩინე საქართველო')]", "მთავარ გვერდზე შესვლა")

    def __init__(self):
        super().__init__(By.XPATH, "//div[@class='why_georgia_hero_content']",
                         "რატომ საქართველოზე შესვლა")

    def batumi_is_visible(self):
        locator = By.XPATH, self.__batumi_visible.locator
        DriverUtils.wait_for_clickable(locator)
        assert self.__batumi_visible.is_visible(), "ვერშევიდა 'ბათუმის' გვერდზე"

    def qutaisi_is_visible(self):
        locator = By.XPATH, self.__qutaisi_visible.locator
        DriverUtils.wait_for_clickable(locator)
        assert self.__qutaisi_visible.is_visible(), "ვერშევიდა 'ქუთაისის' გვერდზე"

    def tbilisi_is_visible(self):
        locator = By.XPATH, self.__tbilisi_visible.locator
        DriverUtils.wait_for_clickable(locator)
        assert self.__tbilisi_visible.is_visible(), "ვერშევიდა 'თბილისის' გვერდზე"

    def geography_is_visible(self):
        locator = By.XPATH, self.__geography_visible.locator
        DriverUtils.wait_for_clickable(locator)
        assert self.__geography_visible.is_visible(), "ვერშევიდა 'საქართველოს გეოგრაფია' ს გვერდზე"

    def seasons_is_visible(self):
        locator = By.XPATH, self.__seasons_visible.locator
        DriverUtils.wait_for_clickable(locator)
        assert self.__seasons_visible.is_visible(), "ვერშევიდა 'სეზონურობა საქართველოში' ს გვერდზე"

    def wine_is_visible(self):
        locator = By.XPATH, self.__wine_visible.locator
        DriverUtils.wait_for_clickable(locator)
        assert self.__wine_visible.is_visible(), "ვერშევიდა 'საქართველო - ღვინის აკვანი' ს გვერდზე"

    def alphabet_is_visible(self):
        locator = By.XPATH, self.__alphabet_visible.locator
        DriverUtils.wait_for_clickable(locator)
        assert self.__alphabet_visible.is_visible(), "ვერშევიდა 'უნიკალური ქართული ანბანი' ს გვერდზე"

    def kitchen_is_visible(self):
        locator = By.XPATH, self.__kitchen_visible.locator
        DriverUtils.wait_for_clickable(locator)
        assert self.__kitchen_visible.is_visible(), "ვერშევიდა 'უგემრიელესი ქართული სამზარეულო' ს გვერდზე"

    def music_is_visible(self):
        locator = By.XPATH, self.__music_visible.locator
        DriverUtils.wait_for_clickable(locator)
        assert self.__music_visible.is_visible(), "ვერშევიდა 'უნიკალური ქართული ფოლკლორი' ს გვერდზე"

    def dance_is_visible(self):
        locator = By.XPATH, self.__dance_visible.locator
        DriverUtils.wait_for_clickable(locator)
        assert self.__dance_visible.is_visible(), "ვერშევიდა 'ქართული ცეკვა' ს გვერდზე"

    def history_is_visible(self):
        locator = By.XPATH, self.__history_visible.locator
        DriverUtils.wait_for_clickable(locator)
        assert self.__history_visible.is_visible(), "ვერშევიდა 'საქართველოს ისტორია' ს გვერდზე"

    def civilisation_is_visible(self):
        locator = By.XPATH, self.__civilisation_visible.locator
        DriverUtils.wait_for_clickable(locator)
        assert self.__civilisation_visible.is_visible(), "ვერშევიდა 'პირველი ევროპული ცივილიზაცია' ს გვერდზე"

    def highest_is_visible(self):
        locator = By.XPATH, self.__highest_visible.locator
        DriverUtils.wait_for_clickable(locator)
        assert self.__highest_visible.is_visible(), "ვერშევიდა 'მაღალი დასახლებული პუნქტი საქართველოში' ს გვერდზე"

    def travel_is_visible(self):
        locator = By.XPATH, self.__travel_visible.locator
        DriverUtils.wait_for_clickable(locator)
        assert self.__travel_visible.is_visible(), "ვერშევიდა 'მთავარი' ს გვერდზე"

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

    def visible_winter(self):
        locator = By.XPATH, self.__winter.locator
        DriverUtils.wait_for_clickable(locator)
        self.__winter.is_visible()

    def visible_summer(self):
        locator = By.XPATH, self.__summer.locator
        DriverUtils.wait_for_clickable(locator)
        self.__summer.is_visible()

    def visible_fall(self):
        locator = By.XPATH, self.__fall.locator
        DriverUtils.wait_for_clickable(locator)
        self.__fall.is_visible()

    def visible_spring(self):
        locator = By.XPATH, self.__spring.locator
        DriverUtils.wait_for_clickable(locator)
        self.__spring.is_visible()

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
