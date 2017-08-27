# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_go(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_test_go(self):
        success = True
        wd = self.wd
        wd.get("https://timeweb.com/ru/")
        wd.find_element_by_link_text('/ru/services/hosting/').click()
        wd.find_element_by_id("mailbox__login").clear()
        wd.find_element_by_id("mailbox__login").send_keys("stas134")
        wd.find_element_by_id("mailbox__password").click()
        wd.find_element_by_id("mailbox__password").clear()
        wd.find_element_by_id("mailbox__password").send_keys("Hermes100.")
        if wd.find_element_by_id("mailbox__auth__remember__checkbox").is_selected():
            wd.find_element_by_id("mailbox__auth__remember__checkbox").click()
        wd.find_element_by_id("mailbox__auth__button").click()
        wd.find_element_by_link_text("Написать письмо").click()
        wd.find_element_by_id("PH_logoutLink").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
