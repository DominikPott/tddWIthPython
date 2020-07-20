import unittest

from selenium import webdriver


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has head aboub a cool new online to-do app. She goes
        # to che out its homepage
        self.browser.get('http://localhost:8000')

        # She notices a page title and header mention to-do lists
        self.assertIn("To-Do", self.browser.title)
        self.fail('Finish the test!')

        # She is invited to enter a to-do item straight awaz

        # She types "Buy peacock feathers" into a text box *Ediths hobby
        # is tying fly-fishing lures)

        # When she hits enter, a page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list

        # There is still a textbox inviting her do add another item. The
        # enters "Use peacock feathers to make a fly" Edith is very methodical

        # The page updates again and now shows both items on her list
        # Edith wonders whether the site will remember her list. Then she sees
        # that the side has generates a unique URL for her -- there is some
        # explanatory text to that effect.

        # She visits that URL - her to-do lists is still there.

        # Satisfied, she goes back to sleep


if __name__ == '__main__':
    unittest.main(warnings='ignore')
