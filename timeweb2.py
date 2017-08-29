# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class timeweb2(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_timeweb2(self):
        wd = self.wd
        self.open_home_page(wd)
        self.tariff_plan(wd)
        self.login(wd, username = "Чернядьева Анна Константиновна", email = "akchernyadeva@gmail.com")

    def login(self, wd, username, email):
        wd.find_element_by_xpath(
            "//div[@class='overlay']/div/div/div[14]/form/div[2]/div[1]/div[2]/div[2]/input").click()
        wd.find_element_by_xpath(
            "//div[@class='overlay']/div/div/div[14]/form/div[2]/div[1]/div[2]/div[2]/input").clear()
        wd.find_element_by_xpath(
            "//div[@class='overlay']/div/div/div[14]/form/div[2]/div[1]/div[2]/div[2]/input").send_keys(
            username)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(email)
        wd.find_element_by_xpath("//label[@for='c4']").click()
        if not wd.find_element_by_id("c4").is_selected():
            wd.find_element_by_id("c4").click()
        wd.find_element_by_link_text("ЗАКАЗАТЬ").click()

    def tariff_plan(self, wd):
        wd.find_element_by_link_text("ХОСТИНГ").click()
        wd.find_element_by_link_text("РАЗМЕСТИТЬ САЙТ").click()
        wd.find_element_by_css_selector("li.item.selected").click()

    def open_home_page(self, wd):
        wd.get("https://timeweb.com/ru/")

    # Check for compliance with the selected plan
    def check_exists_by_link_text("Year+"):
        return len(webdriver.find_elements_by_link_text("Year+")) > 0

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
