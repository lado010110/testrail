import time

from pages.choose_ur_experience_page import ChooseUrExperiencePage
from pages.main_page import MainPage
from pages.sights_page import SightsPage
from utils.DriverUtils import DriverUtils


class ChooseUrExperienceSteps:
    @staticmethod
    def choose_ur_experience():
        main_page = MainPage()
        main_page.is_visible()
        main_page.close_ri_line()
        main_page.click_sights_menu()
        sights_page = SightsPage()
        sights_page.is_visible()
        sights_page.click_to_chat()
        sights_page.click_to_chat()
        sights_page.click_choose_ur_experience()
        choose_page = ChooseUrExperiencePage()
        choose_page.is_visible()
        choose_page.click_category()
        choose_page.click_statue()
        choose_page.click_search()
        choose_page.click_show_more()
        choose_page.click_statue_cate_castles()
        choose_page.click_statue_cate_alc()
        choose_page.click_statue_cate_history()
        choose_page.click_statue_cate_holy()
        DriverUtils.scroll_up()
        choose_page.click_category()
        choose_page.click_art_cult()
        choose_page.click_search()
        time.sleep(10)
