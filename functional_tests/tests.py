from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        #Saria is developing some better time management practices
        #she checks out our awesome to-do list homepage
        self.browser.get('http://localhost:8000')

        #Saria happily notes that the page title mentions "to-do lists"
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #The page prompts her to enter a to-do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        #She types "Teach Link Awesome New Orcarina Song" into the text box
        inputbox.send_keys('Teach Link Awesome New Orcarina Song')

        #When she types enter, the page updates, and now the page lists
        #"1: Teach Link awesome new orcarina song" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Teach Link Awesome New Orcarina Song')

        #There is still a text box for adding an additional item to the list
        #She enters "Check out decrepit Forest Temple"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Check out decrepit Forest Temple')
        inputbox.send_keys(Keys.ENTER)

        #The page updates again showing both items
        self.check_for_row_in_list_table('1: Teach Link Awesome New Orcarina Song')
        self.check_for_row_in_list_table('2: Check out decrepit Forest Temple')

        #Saria is curious if she can come back later to add to the list after 
        #she figures out what is going on in the forest temple -- she notices
        #that the site created a unique url for her list and informs her of this
        self.fail('Finish the test!')

#She visits the url in a private window -- it's still there!

#Satisfied she goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
