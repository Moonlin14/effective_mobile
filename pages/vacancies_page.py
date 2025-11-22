from selenium.webdriver.remote.webdriver import WebDriver
import allure

class VacanciesPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self):
        with allure.step('Switch to vacancies page'):
            self.driver.switch_to.window(self.driver.window_handles[-1])

    def check_what_page_is_open(self):
        with allure.step('Check what page is open by compare urls'):
            assert self.driver.current_url == 'https://ai-hunt.ru/vacancies/'
