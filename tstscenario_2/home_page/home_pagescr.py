from base_page import BasePage
from tstscenario_2.locators.locators_1 import MainPageLocatorsSc2


class HomePageScr(BasePage):
    @property
    def city_field_element(self):
        return self.get_element_present(*MainPageLocatorsSc2.CITY_FIELD)

    @property
    def city_popup_elements(self):
        return self.get_element_present(*MainPageLocatorsSc2.VISIBLE_CITY_FIELD)

    @property
    def city_list_elements(self):
        return self.get_element_present(*MainPageLocatorsSc2.CITY_CHOOSE)

    @property
    def calendar_field_out(self):
        return self.get_element_present(*MainPageLocatorsSc2.CALENDAR_FIELD_CHECKOUT)

    @property
    def calendar_field_in(self):
        return self.get_element_present(*MainPageLocatorsSc2.CALENDAR_FIELD_CHECKIN)

    @property
    def calendar_today_data(self):
        return self.get_element_present(*MainPageLocatorsSc2.TODAY_CALENDAR_DATA)

    @property
    def calendar_next_day_data(self):
        return self.get_element_present(*MainPageLocatorsSc2.ANY_DAY)

    @property
    def search_button_selection(self):
        return self.get_element_present(*MainPageLocatorsSc2.SEARCH_BUTTON)

    @property
    def open_next_page(self):
        return self.get_element_present(*MainPageLocatorsSc2.NEXT_PAGE_INDICATOR)


