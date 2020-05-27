import unittest

from selenium import webdriver


class TestWeb(unittest.TestCase):

    def setUp(self):

        self.browser = webdriver.Firefox()

    def tearDown(self):

        self.browser.quit()

    def test_country_name_in_nav_bar_is_spain(self):

        """Test method that asserts element text is equal to SPAIN"""

        self.browser.get('https://www.alten.es')
        # Use xpath to find element
        self.x_path = "//div[@class='in-the-world']//span[@class='title']"
        self.span = self.browser.find_element_by_xpath(self.x_path)
        self.assertEqual(self.span.text, 'SPAIN')

    def test_country_name_in_nav_bar_is_not_spain(self):

        """Test method that asserts element text is not equal to FRANCE"""

        self.browser.get('https://www.alten.es')
        self.x_path = "//div[@class='in-the-world']//span[@class='title']"
        self.span = self.browser.find_element_by_xpath(self.x_path)
        self.assertNotEqual(self.span.text, 'FRANCE')

    def test_get_and_list_all_sub_elements_in_sectors_tab_on_home_page(self):

        """Test method to display content of sub menu. Assert certain sub-menu values"""

        self.browser.get('https://www.alten.es')
        # First find element by xpath which contains text "Sectores" and click it
        self.x_path_sector = "//a[text()='Sectores']"
        self.browser.find_element_by_xpath(self.x_path_sector).click()
        # Then find sub menu ul
        self.x_path_ul = "//a[text()='Sectores']/following-sibling::ul"
        self.ul_elem = self.browser.find_element_by_xpath(self.x_path_ul)
        # Get all child elements (li) for ul element
        self.li_elems = self.ul_elem.find_elements_by_tag_name('li')
        # Run assertions to check if content is equal for first and last items (this will fail if html design is
        # changed)
        self.assertEqual(self.li_elems[0].text, 'Aeronáutica – Espacio')
        self.assertEqual(self.li_elems[-1].text, 'Servicios financieros – Banca – Seguros – Media')
        # Print items to console
        for item in self.li_elems:
            print(item.text)


if __name__ == '__main__':
    unittest.main()
