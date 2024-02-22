from pages.main_page import MainPage
from pages.map_page import MapPage


class MapSteps:
    @staticmethod
    def map():
        main_page = MainPage()
        main_page.click_map_menu()
        map_page = MapPage()
        map_page.is_visible()
        map_page.screenshot_map()
        map_page.click_more_toggle_places()
        map_page.click_more_toggle_imereti()
        map_page.click_sairme()
        map_page.click_more_toggle_imereti()
        map_page.click_more_toggle_places()
        map_page.click_more_toggle_sights()
        map_page.click_more_toggle_statue()
        map_page.click_castle()
        map_page.click_more_toggle_statue()
        map_page.click_more_toggle_sights()
