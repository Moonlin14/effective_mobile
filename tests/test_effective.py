from pages.home_page import HomePage
from pages.vacancies_page import VacanciesPage

def test_vacancies_page(driver):
    home_page = HomePage(driver)
    vacancies_page = VacanciesPage(driver)
    home_page.click_current_vacancies()
    vacancies_page.open_page()
    vacancies_page.check_what_page_is_open()

def test_leave_a_request_button(driver):
    home_page = HomePage(driver)
    home_page.click_leave_a_request()
    home_page.check_scroll_to_contact_form()

def test_find_out_more(driver):
    home_page = HomePage(driver)
    home_page.click_find_out_more()
    home_page.check_scroll_to_the_cooperation_formats()