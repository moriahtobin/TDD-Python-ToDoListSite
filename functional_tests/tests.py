from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(LiveServerTestCase):
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
        self.browser.get(self.live_server_url)

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

        #When she types enter, she is taken to a new URL
        #the page updates, and now the page lists
        #"1: Teach Link awesome new orcarina song" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        saria_list_url = self.browser.current_url
        self.assertRegex(saria_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Teach Link Awesome New Orcarina Song')

        #There is still a text box for adding an additional item to the list
        #She enters "Check out decrepit Forest Temple"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Check out decrepit Forest Temple')
        inputbox.send_keys(Keys.ENTER)

        #The page updates again showing both items
        self.check_for_row_in_list_table('1: Teach Link Awesome New Orcarina Song')
        self.check_for_row_in_list_table('2: Check out decrepit Forest Temple')

        #Saria sets off to figure out what is going on in the forest temple
        #Happy with her list making experience, she tells her friend Nabooru
        #Nabooru, a new user, decides to visit the site

        ## We open a new browser session, to ensure none of Saria's
        ## information is coming through from cookies etc.
        self.browser.quit()
        self.browser = webdriver.Firefox()

        #Nabooru visits the home page. There is no sign of Saria's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Teach Link Awesome New Orcarina Song', page_text)
        self.assertNotIn('Check out decrepit Forest Temple', page_text)

        #Nabooru starts a new list by entering a new item.
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Steal Silver Gauntlets from Spirit Temple')
        inputbox.send_keys(Keys.ENTER)

        #Nabooru gets her own unique URL
        nabooru_list_url = self.browser.current_url
        self.assertRegex(nabooru_list_url, '/lists/.+')
        self.assertNotEqual(nabooru_list_url, saria_list_url)

        #Nabooru's new url still doesn't see anything of Saria's
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Teach Link Awesome New Orcarina Song', page_text)
        self.assertIn('Steal Silver Gauntlets from Spirit Temple', page_text)

#Saria is curious if she can come back later to add to the list after 
#she figures out what is going on in the forest temple -- she notices
#that the site created a unique url for her list and informs her of this
#self.fail('Finish the test!')

#She visits the url in a private window -- it's still there!

#Satisfied she goes back to sleep
