import time

from pages.curse_landing_page import CurseLandingPage


class CurseLandingSteps:
    @staticmethod
    def curselandingsteps():
        curse_page = CurseLandingPage()
        curse_page.is_visible()
        curse_page.create_new_acc_click()
        time.sleep(10)
        curse_page.first_name_fill()
        time.sleep(5)