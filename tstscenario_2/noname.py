# import Integer as Integer
# from selenium import webdriver
# import unittest
# import time
#
# print("\nstart chrome browser for test..")
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(30)
#
# # driver.get("https://trading.alfa-one-capital.com")
# #
# # driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[4]/a[1]').click()
# # driver.find_element_by_name('first_name').send_keys('Mark1')
# # driver.find_element_by_name('last_name').send_keys('POlo')
# # driver.find_element_by_name('email').send_keys('mark1sw@mail.ru')
# # driver.find_element_by_name('phone').send_keys('123345671')
# # driver.find_element_by_name('password').send_keys('123456781')
# # driver.find_element_by_name('password_confirmation').send_keys('123456781')
# # driver.find_element_by_class_name('form-checkbox').click()
# # # time.sleep(10)
# # driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[8]/button').click()
# #
# # driver.find_element_by_id("//div[@class='bui-calendar__wrapper']").click()
# # elements = driver.find_elements_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr/td/a")
# # for dates in elements:
# #     if (dates.is_enabled() and dates.is_displayed() and str(dates.get_attribute("innerText")) == "10"):
# #         dates.click()
# from lib2to3.pgen2 import driver
#
# import pytest
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# import time
#
#
# class TestSiteFunct():
#     def test_click_on_the_button(self, chrome_drv):
#         time.sleep(3)
#         driver.find_element_by_xpath('//*[@id="xp__guests__toggle"]').click() #  click on button
#         BTN_CLICK = driver.find_element_by_xpath('//button[@aria-label="Increase number of Children"]')
#         time.sleep(2)
#         actions = ActionChains(driver)
#         actions.double_click(BTN_CLICK).perform()  # double click on button
#
#     def test_click_on_the_selection_1(self):
#         #  click on age selection_1
#         time.sleep(2)
#         DATA_GROUP_CHILD_AGE = driver.find_element_by_xpath("//select[@aria-label='Child 1 age']") \
#             .click()  # click on age selection
#         CHILD_AGE_SELECTION = driver.find_element_by_xpath('//select[@aria-label="Child 1 age"]//'
#                                                            'option[@value="10"]'
#                                                            '[normalize-space()="10 years old"]').click()
#     def test_click_on_the_selection_1(self):
#         time.sleep(2)
#         #  click on age selection_2
#         DATA_GROUP_CHILD_AGE_2 = driver.find_element_by_xpath("//select[@aria-label='Child 2 age']") \
#             .click()  # click on age selection
#         CHILD_AGE_SELECTION_1 = driver.find_element_by_xpath('//select[@aria-label="Child 2 age"]//'
#                                                              'option[@value="5"]'
#                                                              '[normalize-space()="5 years old"]').click()
#         EMPTY_FIELD = driver.find_element_by_xpath('//div[@class="xpi__searchbox '
#                                                    'js-ds-layout-events-search-form"]').click()  # click on empty field
#
