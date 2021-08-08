# pytest --tb=line -v test_main_page.py

from pages.main_page import MainPage


def test_main_page(browser):
    link = "https://matchtv.ru/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_part_of_header()
    page.should_be_types_of_sports()

