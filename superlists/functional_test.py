import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(10)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has head aboub a cool new online to-do app. She goes
        # to che out its homepage
        self.browser.get('http://localhost:8000')

        # She notices a page title and header mention to-do lists
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element_by_tag_name("h1").text
        self.assertIn("To-Do", header_text)

        # She is invited to enter a to-do item straight awaz
        inputbox = self.browser.find_element_by_id("id_new_item")
        self.assertEqual(inputbox.get_attribute("placeholder"), "Enter a to-do item")

        # She types "Buy peacock feathers" into a text box *Ediths hobby
        # is tying fly-fishing lures)
        inputbox.send_keys("Buy peacock feathers")

        # When she hits enter, a page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        WebDriverWait(self.browser, 10).until(
            expected_conditions.text_to_be_present_in_element(
                (By.ID, 'id_list_table'), 'Buy peacock feathers')
        )

        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # There is still a textbox inviting her do add another item. The
        # enters "Use peacock feathers to make a fly" Edith is very methodical
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')

        inputbox.send_keys(Keys.ENTER)
        WebDriverWait(self.browser, 10).until(
            expected_conditions.text_to_be_present_in_element(
                (By.ID, 'id_list_table'), 'Use peacock feathers to make a fly')
        )

        # The page updates again and now shows both items on her list
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')


        # Edith wonders whether the site will remember her list. Then she sees
        # that the side has generates a unique URL for her -- there is some
        # explanatory text to that effect.
        self.fail("Finish the test!")
        # She visits that URL - her to-do lists is still there.

        # Satisfied, she goes back to sleep


if __name__ == '__main__':
    unittest.main(warnings='ignore')
