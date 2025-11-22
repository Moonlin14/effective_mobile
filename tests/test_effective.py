from pages.home_page import HomePage
from pages.vacancies_page import VacanciesPage
import allure
from time import sleep

@allure.feature('Header buttons')
def test_vacancies_page(driver):
    home_page = HomePage(driver)
    vacancies_page = VacanciesPage(driver)
    home_page.click_current_vacancies()
    vacancies_page.open_page()
    vacancies_page.check_what_page_is_open()

@allure.feature('Header buttons')
def test_leave_a_request_button(driver):
    home_page = HomePage(driver)
    home_page.click_leave_a_request()
    home_page.check_scroll_to_contact_form()

@allure.feature('Header buttons')
def test_find_out_more(driver):
    home_page = HomePage(driver)
    home_page.click_find_out_more()
    home_page.check_scroll_to_the_cooperation_formats()

@allure.feature('Company buttons in footer')
def test_about_us_button(driver):
    home_page = HomePage(driver)
    home_page.scroll_to_the_footer()
    home_page.click_about_us()
    home_page.check_url('https://www.effective-mobile.ru/#about')

@allure.feature('Company buttons in footer')
def test_vacancies_button(driver):
    home_page = HomePage(driver)
    home_page.scroll_to_the_footer()
    home_page.click_vacancies_button()
    home_page.check_url('https://www.effective-mobile.ru/#specializations')

@allure.feature('Company buttons in footer')
def test_testimonials_button(driver):
    home_page = HomePage(driver)
    home_page.scroll_to_the_footer()
    home_page.click_testimonials_button()
    home_page.check_url('https://www.effective-mobile.ru/#testimonials')

@allure.feature('Company buttons in footer')
def test_contacts_button(driver):
    home_page = HomePage(driver)
    home_page.scroll_to_the_footer()
    home_page.click_conctacts_button()
    home_page.check_url('https://www.effective-mobile.ru/#contact')
    home_page.check_scroll_to_contact_form()

@allure.feature('Services buttons in footer')
def test_outstaff_button(driver):
    home_page = HomePage(driver)
    home_page.scroll_to_the_footer()
    home_page.click_outstaff_button()
    home_page.check_scroll_to_the_cooperation_formats()
    home_page.check_url('https://www.effective-mobile.ru/#services')

@allure.feature('Services buttons in footer')
def test_employment_button(driver):
    home_page = HomePage(driver)
    home_page.scroll_to_the_footer()
    home_page.click_employment_button()
    home_page.check_scroll_to_the_cooperation_formats()
    home_page.check_url('https://www.effective-mobile.ru/#services')

@allure.feature('Services buttons in footer')
def test_consultation_button(driver):
    home_page = HomePage(driver)
    home_page.scroll_to_the_footer()
    home_page.click_consultation_button()
    home_page.check_scroll_to_contact_form()
    home_page.check_url('https://www.effective-mobile.ru/#contact')

@allure.feature('Cooperation formats')
def test_outstaff_button_in_cooperation_formats(driver):
    home_page = HomePage(driver)
    home_page.scroll_to_the_cooperation_formats()
    home_page.click_outstaff_button_in_cooperation_formats()
    home_page.check_scroll_to_contact_form()

@allure.feature('Cooperation formats')
def test_employment_assistance_button_in_cooperation_formats(driver):
    home_page = HomePage(driver)
    home_page.scroll_to_the_cooperation_formats()
    home_page.click_employment_assistance_button_in_cooperation_formats()
    home_page.check_scroll_to_contact_form()