from selenium.webdriver.common.by import By

from elements.button import Button
from elements.element import Element
from pages.base_form import BaseForm
from utils.DriverUtils import DriverUtils


class ChooseUrExperiencePage(BaseForm):
    __search = Button(By.XPATH,
                      "//button[@class='ExperienceIndexPageFilters_ExperienceIndexPageFilters__Button__kkPXE']",
                      "სერჩი")
    __category = Button(By.XPATH, "(//div[contains(@class,'css-4g6ai3')])[1]", "კატეგორიაზე დაკლიკება")
    __statues = Button(By.XPATH, "//div[contains(text(),'კულტურული ძეგლები')]", "კულტურული ძეგლები")
    __art_cult = Button(By.XPATH, "//div[contains(text(),'ხელოვნება და კულტურა')]", "კულტურული ძეგლები")
    __show_more = Button(By.XPATH, "//button[contains(text(),'მეტის ჩატვირთვა')]", "მედის ნახვის ღილაკი")
    __statues_cate_castles = Element(By.XPATH, "//li[contains(text(),'ციხესიმაგრეები')]", "ციხესიმაგრები")
    __statues_cate_alc = Element(By.XPATH, "//li[contains(text(),'არქეოლოგიური ძეგლები')]", "არქეოლოგიური ძეგლები")
    __statues_cate_history = Element(By.XPATH, "//li[contains(text(),'ისტორიული ძეგლები')]", "ისტორიული ძეგლები")
    __statues_cate_holy = Element(By.XPATH, "//li[contains(text(),'წმინდა ადგილები')]", "წმინდა ადგილები")

    def __init__(self):
        super().__init__(By.XPATH, "//p[contains(text(),'აღმოაჩინე შენთვის სასურველი სანახაობა მთელი საქართ')]",
                         "შექმენიშენი თავგადავლის გვერდზე შესვლა")

    def click_search(self):
        locator = By.XPATH, self.__search.locator
        DriverUtils.wait_for_clickable(locator)
        self.__search.click()

    def click_show_more(self):
        locator = By.XPATH, self.__show_more.locator
        DriverUtils.wait_for_clickable(locator)
        self.__show_more.click()

    def click_category(self):
        locator = By.XPATH, self.__category.locator
        DriverUtils.wait_for_clickable(locator)
        self.__category.click()

    def click_statue(self):
        locator = By.XPATH, self.__statues.locator
        DriverUtils.wait_for_clickable(locator)
        self.__statues.click()

    def click_statue_cate_castles(self):
        locator = By.XPATH, self.__statues_cate_castles.locator
        DriverUtils.wait_for_clickable(locator)
        self.__statues_cate_castles.click()

    def click_statue_cate_alc(self):
        locator = By.XPATH, self.__statues_cate_alc.locator
        DriverUtils.wait_for_clickable(locator)
        self.__statues_cate_alc.click()

    def click_statue_cate_history(self):
        locator = By.XPATH, self.__statues_cate_history.locator
        DriverUtils.wait_for_clickable(locator)
        self.__statues_cate_history.click()

    def click_statue_cate_holy(self):
        locator = By.XPATH, self.__statues_cate_holy.locator
        DriverUtils.wait_for_clickable(locator)
        self.__statues_cate_holy.click()

    def click_art_cult(self):
        locator = By.XPATH, self.__art_cult.locator
        DriverUtils.wait_for_clickable(locator)
        self.__art_cult.click()
