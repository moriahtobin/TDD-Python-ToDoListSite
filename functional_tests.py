from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #Saria is developing some better time management practices
        #she checks out our awesome to-do list homepage
        self.browser.get('http://localhost:8000')

        #Saria happily notes that the page title mentions "to-do lists"
        self.assertIn('To-Do', self.browser.title)
        self.fail("Finish the test!")

#The page prompts her to enter a to-do item

#She types "Teach Link Awesome New Orcarina Song" into the text box

#When she types enter, the page updates, and now the page lists
#"1: Teach Link awesome new orcarina song" as an item in a to-do list

#There is still a text box for adding an additional item to the list
#She enters "Check out decrepit Forest Temple"

#The page updates again showing both items

#Saria is curious if she can come back later to add to the list after 
#she figures out what is going on in the forest temple -- she notices
#that the site created a unique url for her list and informs her of this

#She visits the url in a private window -- it's still there!

#Satisfied she goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
