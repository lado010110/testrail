import time

from pages.imereti_page import ImeretiPage
from pages.main_page import MainPage
from pages.places_page import PlacesPage
from utils.DriverUtils import DriverUtils


class PlacesMapSteps:
    @staticmethod
    def places_map():
        main_page = MainPage()
        main_page.click_places_button()
        places_page = PlacesPage()
        places_page.is_visible()
        places_page.scroll_down_to_imereti()
        DriverUtils.scroll_down()
        time.sleep(4)
        places_page.click_imereti()
        imereti_page = ImeretiPage()
        imereti_page.move_to_map()
        imereti_page.is_visible()
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
