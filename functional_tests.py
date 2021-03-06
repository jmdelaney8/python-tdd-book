from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        #Gary is using his cool new to do list
        self.browser.get('http://localhost:8000')

        #Does the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        
        #she is invited right away to enter a to do
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')
        
        #she type in "buy feathers" and hits enter
        inputbox.send_keys('Buy peacock feathers')
        
        #the page updates showing her to do
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # and a box inviting her to add another to do
        #she types "use feathers to make fly" and hits enter
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feather to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        #The page updates with her two to-dos
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use a peacock feather to make a fly')
        #there is a uniquely generated URL for her and some explanatory text about how to reach this to-do list again
        self.fail('finish the test') 
        #she visits that URL and the to-do list is still there

        #satisfied, she closes the browser

if __name__ == '__main__':
    unittest.main(warnings='ignore')
