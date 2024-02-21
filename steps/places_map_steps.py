import time

from pages.imereti_page import ImeretiPage
from pages.main_page import MainPage
from pages.places_page import PlacesPage


class PlacesMapSteps:
    @staticmethod
    def places_map():
        main_page = MainPage()
        main_page.is_visible()
        main_page.close_ri_line()
        main_page.click_places_button()
        places_page = PlacesPage()
        places_page.is_visible()
        time.sleep(2)
        places_page.scroll_down_to_imereti()
        time.sleep(2)
        places_page.click_imereti()
        time.sleep(2)
        imereti_page = ImeretiPage()
        imereti_page.move_to_map()
        imereti_page.is_visible()
        time.sleep(3)
        imereti_page.screenshot_map()
        imereti_page.click_more_toggle_places()
        imereti_page.click_more_toggle_imereti()
        imereti_page.click_sairme()
        imereti_page.click_more_toggle_imereti()
        imereti_page.click_more_toggle_places()
        imereti_page.click_more_toggle_sights()
        imereti_page.click_more_toggle_statue()
        imereti_page.click_castle()
        imereti_page.click_more_toggle_statue()
        imereti_page.click_more_toggle_sights()
        # imereti_page.move_to_element()
        # imereti_page.click_airports()
        # time.sleep(2)
        # imereti_page.click_tourist()
        # time.sleep(10)
