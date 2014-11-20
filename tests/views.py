from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import resolve
from django.http import HttpRequest
import unittest

from selenium import webdriver

class TestBuilds(unittest.TestCase):
    '''
    Test to see if builds are saved, editable, deletable
    '''
    fixtures = ['initial_data.json']

    def setUp(self):
        """setup function"""
        self.client = Client()
        self.driver = webdriver.Firefox()
        self.base_url = "http://127.0.0.1:8000/builds/new_build/"
        self.verificationErrors = []     

    def test_save_builds(self):
        '''
        Test if builds are saved
        '''    
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("id_moboField").click()
        driver.find_element_by_id("id_moboField").clear()
        driver.find_element_by_id("id_moboField").send_keys("motherboard")
        driver.find_element_by_id("id_cpuField").click()
        driver.find_element_by_id("id_cpuField").clear()
        driver.find_element_by_id("id_cpuField").send_keys("processor")
        driver.find_element_by_id("id_gpuField").click()
        driver.find_element_by_id("id_gpuField").clear()
        driver.find_element_by_id("id_gpuField").send_keys("graphics")
        driver.find_element_by_id("id_caseField").click()
        driver.find_element_by_id("id_caseField").clear()
        driver.find_element_by_id("id_caseField").send_keys("case")
        driver.find_element_by_id("id_memField").click()
        driver.find_element_by_id("id_memField").clear()
        driver.find_element_by_id("id_memField").send_keys("memory")
        driver.find_element_by_id("id_hdField").click()
        driver.find_element_by_id("id_hdField").clear()
        driver.find_element_by_id("id_cpuField").send_keys("hard drive")
        driver.find_element_link_text("Submit Query").click()

    def test_login(self):
        

    def tearDown(self):
        """delete models from test database"""
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ ==  '__main__':
    unittest.main()