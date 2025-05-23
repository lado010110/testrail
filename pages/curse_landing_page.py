from selenium.webdriver.common.by import By

from elements.button import Button
from elements.input import Input
from pages.base_form import BaseForm

from faker import Faker


fake = Faker()
email = fake.email()
password = fake.password()



class CurseLandingPage(BaseForm):

    __create_new_acc = Button(By.XPATH, "//a[normalize-space()='Create a new account']", "რეგისტრაცის ღილაკი")
    __first_name = Input(By.XPATH, "//div[@class='sign-up__wrapper']//div[1]//div[1]//input[1]", "სახელის ველი")

    def __init__(self):
        super().__init__(By.XPATH, "//h2[normalize-space()='Welcome Back!']",
                         "შევიდა ლენდინგ პეიჯზე")

    def create_new_acc_click(self):
        self.__create_new_acc.click()

    def first_name_fill(self):
        self.__first_name.send_text(fake.user_name())
