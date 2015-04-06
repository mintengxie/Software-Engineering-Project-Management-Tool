from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_project_and_create_issue(self):
        # User has heard about a new online PM app. They go
        # to check out its homepage
        self.browser.get(self.live_server_url)
        self.browser.implicitly_wait(10)


        # They notice the page title and header mention Project
        self.assertIn('Project', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Project', header_text)
