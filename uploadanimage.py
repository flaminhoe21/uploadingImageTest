# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest, time, re, os


class assertTesting(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('E:\Flaminhoe\VUM\QA\chromedriver79\chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get(
            "https://media.prod.mdn.mozit.cloud/attachments/2012/07/09/3698/391aef19653595a663cc601c42a67116/image_upload_preview.html")

        driver.find_element_by_id("uploadImage").send_keys("C:\\Users\\Iva Tsaneva\\Desktop\\pug.jfif")
        driver.find_element_by_xpath("//input[@value='Send']").click()

        src = driver.page_source
        text_found = re.search(r'Send', src)
        #self.assertNotEqual(text_found, None)
        self.assertTrue(text_found)

        print(driver.current_url)
        self.assertIn("media", driver.current_url)




    def tearDown(self):
        self.driver.quit()
        pass


if __name__ == "__main__":
    unittest.main()


