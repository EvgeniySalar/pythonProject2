import pytest
from tstscenario_2.Mainpgscr import MainPagescr
from tstscenario_2.home_page.home_pagescr import HomePageScr


class TestSiteFuncScr:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, chrome_drv):
        self.home_page = HomePageScr(chrome_drv)
        self.main_page = MainPagescr(chrome_drv)
        yield chrome_drv

    def test_click_on_city_field(self):
        self.home_page.city_field_element.click()
        self.main_page.citys_field_is_clicked()
        self.home_page.city_list_elements.click()
        # self.main_page.city_is_chosen()

    def test_search_button_click(self):
        self.home_page.search_button_selection.click()
        self.main_page.open_the_next_page()

    def test_calendar_field(self):
        self.home_page.calendar_today_data.click()
        self.home_page.calendar_field_out.click()
        self.home_page.calendar_next_day_data.click()
        self.home_page.search_button_selection.click()

