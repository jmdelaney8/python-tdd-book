from selenium import webdriver
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
        self.fail('Finish the test!')
        
        #she is invited right away to enter a to do

        #she type in "buy feathers" and hits enter

        #the page updates showing her to do and a box inviting her to enter another to do

        #she types "use feathers to make fly" and hits enter

        #there is a uniquely generated URL for her and some explanatory text about how to reach this to-do list again

        #she visits that URL and the to-do list is still there

        #satisfied, she closes the browser

if __name__ == '__main__':
    unittest.main(warnings='ignore')
