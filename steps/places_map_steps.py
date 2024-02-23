
from pages.imereti_page import ImeretiPage
from pages.main_page import MainPage
from pages.map_page import MapPage
from pages.places_page import PlacesPage


class PlacesMapSteps:
    @staticmethod
    def places_map():
        map = MapPage()
        main_page = MainPage()
        main_page.click_places_button()
        places_page = PlacesPage()
        places_page.click_imereti()
        imereti_page = ImeretiPage()
        imereti_page.move_to_map()
        imereti_page.is_visible()
        imereti_page.screenshot_map()
        map.click_more_toggle_places()
        map.click_more_toggle_imereti()
        map.click_sairme()
        map.click_more_toggle_imereti()
        map.click_more_toggle_places()
        map.click_more_toggle_sights()
        map.click_more_toggle_statue()
        map.click_castle()
        map.click_more_toggle_statue()
        map.click_more_toggle_sights()
