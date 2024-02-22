
import pyautogui

from pages.main_page import MainPage
from pages.my_itinerary_page import MyItineraryPage
from pages.search_page import SearchPage
from pages.sights_page import SightsPage


class MyItinerarySteps:
    @staticmethod
    def itinerary_steps():
        gui = pyautogui
        sight_name = "ოკაცეს"
        place_name = "თბილისი"
        activ_name = "ტური ბათუმში"
        tur_name = "ორდღიანი ტური სვანეთში"
        main_page = MainPage()
        sights_page = SightsPage()
        search_page = SearchPage()
        itinerary_page = MyItineraryPage()
        main_page.click_search()
        main_page.fill_search_menu_sight(sight_name)
        gui.press("enter")
        search_page.is_visible()
        search_page.click_sight_canyon()
        sights_page.click_hart_button()
        main_page.click_search()
        main_page.fill_search_menu_activiti(activ_name)
        gui.press("enter")
        search_page.is_visible()
        itinerary_page.click_activ()
        sights_page.click_hart_button()
        main_page.click_search()
        main_page.fill_search_menu_place(place_name)
        gui.press("enter")
        search_page.is_visible()
        search_page.click_sort_pages()
        itinerary_page.click_tbilisi()
        sights_page.click_hart_button()
        main_page.click_search()
        main_page.fill_search_menu_tur(tur_name)
        gui.press("enter")
        search_page.is_visible()
        search_page.click_sort_tur_menu()
        itinerary_page.click_tur()
        sights_page.click_tur_hart_button()
        main_page.click_favorites_menu()
        itinerary_page.is_visible()
        itinerary_page.click_sort_menu_activ()
        itinerary_page.click_sort_menu_places()
        itinerary_page.click_sort_menu_tur()
