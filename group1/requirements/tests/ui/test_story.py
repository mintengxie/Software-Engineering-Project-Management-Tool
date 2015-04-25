from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestStory(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000"
        self.verificationErrors = []
        self.accept_next_alert = True
        
    def test_story_add(self):
        self.home(self.driver)
        self.login(self.driver)
        self.create_project(self.driver)
        self.create_story(self.driver)
        self.delete_project(self.driver)
        self.logout(self.driver)
        
    def home(self, driver):
        driver.get(self.base_url + "/")
        
    def login(self, driver):
        driver.find_element_by_link_text("Sign In").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("pass")
        driver.find_element_by_xpath("//button[@type='submit']").click()

    def create_project(self, driver):
        driver.find_element_by_css_selector("i.glyphicon.glyphicon-plus").click()
        time.sleep(2)
        driver.find_element_by_id("id_title").clear()
        driver.find_element_by_id("id_title").send_keys("___Test Project 1___")
        driver.find_element_by_id("id_description").clear()
        driver.find_element_by_id("id_description").send_keys("___Test Project Description___")
        driver.find_element_by_link_text("Create Project").click()
        time.sleep(2)
        
    def delete_project(self, driver):
        driver.find_element_by_link_text("Dashboard").click()
        driver.find_element_by_xpath("//a[contains(@data-del-proj,'___Test Project 1___')]").click()
        driver.find_element_by_link_text("Delete Project").click()
        time.sleep(2)
    
    def create_story(self, driver):
        driver.find_element_by_xpath("//a[contains(@data-open-proj, '___Test Project 1___')]").click()
        driver.find_element_by_css_selector("i.glyphicon.glyphicon-plus").click()
        driver.find_element_by_xpath("//input[@id='id_title']").clear()
        driver.find_element_by_xpath("//input[@id='id_title']").send_keys("___Test Story 1___")
        driver.find_element_by_xpath("//textarea[@id='id_description']").clear()
        driver.find_element_by_xpath("//textarea[@id='id_description']").send_keys("Description")
        driver.find_element_by_id("id_reason").clear()
        driver.find_element_by_id("id_reason").send_keys("Reason")
        driver.find_element_by_id("id_test").clear()
        driver.find_element_by_id("id_test").send_keys("Test")
        driver.find_element_by_id("id_task_set-0-description").clear()
        driver.find_element_by_id("id_task_set-0-description").send_keys("Task 1")
        Select(driver.find_element_by_id("id_owner")).select_by_visible_text("admin")
        driver.find_element_by_id("id_hours").clear()
        driver.find_element_by_id("id_hours").send_keys("1")
        driver.find_element_by_id("id_hours").clear()
        driver.find_element_by_id("id_hours").send_keys("2")
        driver.find_element_by_id("id_hours").clear()
        driver.find_element_by_id("id_hours").send_keys("3")
        Select(driver.find_element_by_id("id_status")).select_by_visible_text("Started")
        Select(driver.find_element_by_id("id_points")).select_by_visible_text("3 Points")
        driver.find_element_by_link_text("Create User Story").click()
        time.sleep(2)
        return self.assertTrue(self.is_element_present(By.XPATH, "//a[contains(@data-story, '___Test Story 1___')]"))
    
    def logout(self, driver):
        driver.find_element_by_link_text("admin").click()
        driver.find_element_by_link_text("Logout").click()
        driver.find_element_by_link_text("Home").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()