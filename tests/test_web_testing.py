import unittest

from selenium import webdriver


class TestWeb(unittest.TestCase):

    def setUp(self):

        self.browser = webdriver.Firefox()

    def tearDown(self):

        self.browser.quit()

    def test_country_name_in_nav_bar_is_spain(self):
        self.browser.get('https://www.alten.es')
        self.x_path = "//div[@class='in-the-world']//span[@class='title']"
        self.span = self.browser.find_element_by_xpath(self.x_path)
        self.assertEqual(self.span.text, 'SPAIN')



if __name__ == '__main__':
    unittest.main()
