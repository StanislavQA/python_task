# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

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
        success = True
        wd = self.wd
        wd.get("https://timeweb.com/ru/")
        wd.find_element_by_link_text("ХОСТИНГ").click()
        wd.find_element_by_link_text("РАЗМЕСТИТЬ САЙТ").click()
        wd.find_element_by_css_selector("li.item.selected").click()
        wd.find_element_by_xpath("//div[@class='overlay']/div/div/div[14]/form/div[2]/div[1]/div[2]/div[2]/input").click()
        wd.find_element_by_xpath("//div[@class='overlay']/div/div/div[14]/form/div[2]/div[1]/div[2]/div[2]/input").clear()
        wd.find_element_by_xpath("//div[@class='overlay']/div/div/div[14]/form/div[2]/div[1]/div[2]/div[2]/input").send_keys("Иванов Петр Иванович")
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("stas134@bk.ru")
        wd.find_element_by_xpath("//label[@for='c4']").click()
        if not wd.find_element_by_id("c4").is_selected():
            wd.find_element_by_id("c4").click()
        wd.find_element_by_link_text("ЗАКАЗАТЬ").click()
        wd.find_element_by_xpath("//div[2]/div[1]/div[1]/button").click

    def assert_check(self):
        wd.find_element_by_link_text("Year+").text()
        assert "Year" in self.driver.title //проверка на соответствие
        wd.find_element_by_id("ui-id-4").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
