from home_page.home_pagescr import HomePageScr


class MainPagescr(HomePageScr):


    def citys_field_is_clicked(self):
        assert self.city_popup_elements.is_enabled(), "Field is not clicked"
        print("Field is clicked")

    def city_is_chosen(self):
        assert self.city_list_elements.is_enabled(), "City name is not selected"
        print("City name is  selected")

    def open_the_next_page(self):
        assert self.open_next_page.is_displayed(), "Page is not opened"
        print("Page is  opened")


    # def age_button_check(self):
    #     assert self.home_page.calendar_field().is_enabled(), "Age button is not enabled"
    #     print("Age button is enabled")
    #
    # def age_button_change(self):
    #     assert self.home_page.section_elements().is_enabled(), "Button is not enabled"
    #     print("Child age button is enabled")
    #
    # def age_button_change_2(self):
    #     assert self.self.home_page.section_elements_2().is_enabled(), "Age button_2 is not enabled"
    #     print("Age button_2 is enabled")
    #
    # def age_button_change_2(self):
    #     assert self.home_page.section_child_age_element_2().is_enabled(), "Button_2 is not enabled"
    #     print("Child age button_2 is enabled")
    #
    # def enable_empty_field(self):
    #     assert self.home_page.empty_field().is_enabled(), "Empty field is not clicked"
    #     print("Empty field is clicked")
    #
    #
    #
    # def is_displayed_basket_button(self):
    #
    #     assert self.home_page.section_child_age_element().is_enabled()
