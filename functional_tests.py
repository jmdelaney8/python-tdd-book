from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

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
        inputbox.send_keys('Buy peakcock feathers')
        
        #the page updates showing her to do
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        # and a box inviting her to add another to do
        self.fail('Finish the test!')
        
        #she types "use feathers to make fly" and hits enter

        #there is a uniquely generated URL for her and some explanatory text about how to reach this to-do list again

        #she visits that URL and the to-do list is still there

        #satisfied, she closes the browser

if __name__ == '__main__':
    unittest.main(warnings='ignore')
