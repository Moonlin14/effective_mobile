from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import allure

class HomePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click_leave_a_request(self):
        with allure.step('Click on leave a request button'):
            button = self.driver.find_element(By.XPATH, '//button[text()="Оставить заявку"]')
            button.click()

    def click_find_out_more(self):
        with allure.step('Click on find out more button in footer'):
            button = self.driver.find_element(By.XPATH, '//button[text()="Узнать больше"]')
            button.click()
    
    def click_current_vacancies(self):
        with allure.step('Click on current vacancies button'):
            button = self.driver.find_element(By.XPATH, '//a[text()="Актуальные вакансии"]')
            button.click()

    def scroll_to_the_footer(self):
        with allure.step('Scroll to the footer'):
            footer = self.driver.find_element(By.CSS_SELECTOR, 'footer')
            ActionChains(self.driver).scroll_to_element(footer).perform()

    def click_about_us(self):
        with allure.step('Click on about us'):
            button = self.driver.find_element(By.XPATH, '//a[text()="О нас"]')
            button.click()

    def check_url(self, url_to_check):
        with allure.step('Check that url equal expected url'):
            url = self.driver.current_url
            assert url == url_to_check

    def check_scroll_to_contact_form(self):
        with allure.step('Check that click on leave a request button, scrolling to contact form'):
            WebDriverWait(self.driver, 6).until(EC.visibility_of_element_located((By.XPATH, '//h2[text()="Свяжитесь с нами"]')))
            assert self.driver.find_element(By.XPATH, '//h2[text()="Свяжитесь с нами"]').is_displayed()

    
    def check_scroll_to_the_cooperation_formats(self):
        with allure.step('Check that click on find out more button, scrolling to cooperation formats'):
            WebDriverWait(self.driver, 6).until(EC.visibility_of_element_located((By.XPATH, '//h2[text()="Форматы сотрудничества"]')))
            assert self.driver.find_element(By.XPATH, '//h2[text()="Форматы сотрудничества"]').is_displayed()

    def click_vacancies_button(self):
        with allure.step('Click vacancies button in footer'):
            button = self.driver.find_element(By.XPATH, '//a[text()="Вакансии"]')
            button.click()

    def click_testimonials_button(self):
        with allure.step('Click testimonials button in footer'):
            button = self.driver.find_element(By.XPATH,  '//a[text()="Отзывы"]')
            button.click()

    def click_conctacts_button(self):
        with allure.step('Click contacts button in footer'):
            button = self.driver.find_element(By.XPATH, '//a[text()="Контакты"]')
            button.click()

    def click_outstaff_button(self):
        with allure.step('Click outstaff button in footer'):
            button = self.driver.find_element(By.XPATH, '//a[text()="Аутстафф"]')
            button.click()

    def click_employment_button(self):
        with allure.step('Click employment button in footer'):
            button = self.driver.find_element(By.XPATH, '//a[text()="Трудоустройство"]')
            button.click()

    def click_consultation_button(self):
        with allure.step('Click consultation button in footer'):
            button = self.driver.find_element(By.XPATH, '//a[text()="Консультация"]')
            button.click()
    
    def click_outstaff_button_in_cooperation_formats(self):
        with allure.step('Click outstaff button in cooperation formats'):
            button = self.driver.find_elements(By.XPATH, '//button[text()="Выбрать формат"]')
            button[0].click()

    def click_employment_assistance_button_in_cooperation_formats(self):
        with allure.step('Click employment assistance button in cooperation formats'):
            button = self.driver.find_elements(By.XPATH, '//button[text()="Выбрать формат"]')
            button[1].click()