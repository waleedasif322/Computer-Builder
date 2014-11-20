from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import resolve
from django.http import HttpRequest

import unittest
import re
import requests
from bs4 import BeautifulSoup
import urllib2
import json
from selenium import webdriver
from selenium.webdriver.support.ui import Select

from builds.models import *
from builds.views import *
from parts.models import *

# Create your tests here.

class TestAutocomplete(unittest.TestCase):
    '''
    This class is going to test the builds creation for user story #2 - "As a user I want to be able to make new builds"
    '''
    fixtures = ['parts_test_data.json']

    def setUp(self):
        '''
        setup function
        '''
        self.browser = webdriver.Firefox()
        self.html = BeautifulSoup(urllib2.urlopen('http://127.0.0.1:8000/builds/new_build').read())
    
    def test_autoField_mobo(self):
        '''
        Test if all motherboards from database appear in autocomplete
        '''
        mobos_db = moboListing.objects.all().count()
        r = requests.get('http://127.0.0.1:8000/builds/autocomplete/ajax_lookup/moboListing?term=+')
        s = json.loads(urllib2.urlopen('http://127.0.0.1:8000/builds/autocomplete/ajax_lookup/moboListing?term=+').read())
        #num_mobos_db = len(mobos_db)
        count = 0
        for i in s:
            count += 1
        err = """Different number of items"""
        self.assertEquals(count, mobos_db, err)


    def test_autoField_cpu(self):
        '''
        Test if all Processors from database appear in autocomplete
        '''
        cpus_db = cpuListing.objects.all().count()
        r = requests.get('http://127.0.0.1:8000/builds/autocomplete/ajax_lookup/cpuListing?term=+')
        s = json.loads(urllib2.urlopen('http://127.0.0.1:8000/builds/autocomplete/ajax_lookup/cpuListing?term=+').read())
        #num_mobos_db = len(mobos_db)
        count = 0
        for i in s:
            count += 1
        err = """Different number of items"""
        self.assertEquals(count, cpus_db, err)

    def test_autoField_gpu(self):
        '''
        Test if all Graphics Cards from database appear in autocomplete
        '''
        gpus_db = gpuListing.objects.all().count()
        s = json.loads(urllib2.urlopen('http://127.0.0.1:8000/builds/autocomplete/ajax_lookup/gpuListing?term=+').read())
        count = 0
        for i in s:
            count += 1
        err = """Different number of items"""
        self.assertEquals(count, gpus_db, err)

    def test_autoField_case(self):
        '''
        Test if all Cases from database appear in autocomplete
        '''
        case_db = caseListing.objects.all().count()
        s = json.loads(urllib2.urlopen('http://127.0.0.1:8000/builds/autocomplete/ajax_lookup/caseListing?term=+').read())
        count = 0
        for i in s:
            count += 1
        err = """Different number of items"""
        self.assertEquals(count, case_db, err)

    def test_autoField_mem(self):
        '''
        Test if all Memory from database appear in autocomplete
        '''
        mem_db = memListing.objects.all().count()
        s = json.loads(urllib2.urlopen('http://127.0.0.1:8000/builds/autocomplete/ajax_lookup/memListing?term=+').read())
        count = 0
        for i in s:
            count += 1
        err = """Different number of items"""
        self.assertEquals(count, mem_db, err)

    def test_autoField_hd(self):
        '''
        Test if all Hard Drives from database appear in autocomplete
        '''
        hd_db = hdListing.objects.all().count()
        s = json.loads(urllib2.urlopen('http://127.0.0.1:8000/builds/autocomplete/ajax_lookup/hdListing?term=+').read())
        count = 0
        for i in s:
            count += 1
        err = """Different number of items"""
        self.assertEquals(count, hd_db, err)

    def tearDown(self):
        self.browser.quit()

class BuildsViewsTest(TestCase):
    '''
    test the views
    '''
    fixtures = ['initial_data.json']

    def test_views_home(self):
        """
        Test if the home page shows the saved build correctly
        """
        response = self.client.get("/builds/home/")
        self.assertEqual(response.status_code, 302)
        self.assertTrue('builds' in response.context)
        self.assertEqual([build.pk for build in response.context['builds']], [1])
        build_1 = resp.context['builds'][0]
        self.assertEqual(build_1.name, 'First Build')
        self.assertEqual(build_1.moboPart, ' ASUS M5A78L-M LX PLUS AM3+ AMD 760G + SB710 Micro ATX AMD Motherboard ')
        self.assertEqual(build_1.cpuPart, ' AMD A4-6320 Richland 3.8GHz Socket FM2 65W Desktop Processor AMD Radeon HD8000 Series AD6320OKHLBOX ')
        self.assertEqual(build_1.casePart, ' Thermaltake Commander MS-I Epic Edition Black / Red SECC ATX Mid Tower Computer Case ')
        self.assertEqual(build_1.gpuPart, ' nVIDIA GeForce GT 610 1GB PCI Express PCI-E x16 Single Slot Video Graphics Card  ')
        self.assertEqual(build_1.memPart, ' 2GB (2X1GB) DDR Memory ASUS PC-DL Deluxe ')
        self.assertEqual(build_1.hdPart, ' SAMSUNG 840 EVO MZ-7TE250LW 2.5\" TLC Internal Solid State Drive (SSD) With Notebook Bundle Kit ')
        self.assertEqual(build_1.access_r, 'pub')
        self.assertEqual(build_1.user, 1)

    def test_views_myBuilds(self):
        """
        Test if all our builds show up on our personal builds page
        """
        response = self.client.get("/builds/show/First__Build")
        self.assertEqual(response.status_code, 301)
        self.assertEqual(response.context['abuild'].pk, 1)
        self.assertEqual(response.context['abuild'].name, 'First Build')

        # Ensure that non existent build throws a 404.
        response = self.client.get('/builds/show/Second__Build')
        self.assertEqual(response.status_code, 404)

    def test_views_public(self):
        """
        Test if only public builds show up
        """
        response = self.client.get("/builds/public_builds/")
        self.assertEqual(response.status_code, 302)
        build = BuildsTable.objects.get(pk=1)
        self.assertEqual('pub', build.access_r)

    def test_views_newBuild(self):
        """
        Test if the new build page shows the forms correctly
        """ 
        build = BuildsTable.objects.get(pk=1)
        self.assertEqual(build.buildstable_set.get(pk=1).name, 'First Build')
        response = self.client.post('/builds/new_build/', {'name': 'First Build'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], 'http://testserver/builds/build_confirmation/')

    def test_bad_build(self):
        '''
        Test all bad scenarios in making new build
        '''
        # Ensure a non-existent pk throws a not found
        response = self.client.post('builds/show/not_exist/')
        self.assertEqual(response.context['error'], "Error! It seems like we cannot access this build from our Database.")

        # Sanity Check
        build = BuildsTable.objects.get(pk=1)
        self.assertEqual(build.get(pk=1).name, "First Build")

        # Send no post data.
        response = self.client.post('/builds/new_build/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['error'], "Please fill in all required fields")

        # Send junk post data
        response = self.client.post('/builds/new_build/', {'foo': 'bar'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['error'], "Please fill in all required fields")

        # Send non-existent access_right
        response = self.client.post('/builds/new_build/', {'access_r': 'pro'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['error'], "Please fill in all required fields")

    def test_edit_build(self):
        """
        Test if all the edit builds form works
        """
        response = self.client.get("/builds/edit/")
        self.assertEqual(response.status_code, 302)

    def test_top_rated(self):
        """
        Test if the top rated builds display on home page
        """
        response = self.client.get("/builds/home/")
        self.assertEqual(response.status_code, 302)
        self.assertTrue('builds' in response.context)
        self.assertEqual([build.pk for build in response.context['builds']], 2)
        build_1 = reponse.context['builds'][0]
        build_2 = response.context['builds'][1]
        self.assertGreaterThan(build_1.rating, build_2.rating)

    def test_total_price_build(self):
        """
        Test if the total price is correct for build
        """
        response = self.client.get("/builds/show/First__Build")
        build = response.context['abuild']
        price = build.price
        self.assertEqual(price, 579.99)

    def test_most_recent(self):
        """
        Test if the most recent builds display on home page
        """
        response = self.client.get("/builds/home/")
        self.assertEqual(response.status_code, 302)
        self.assertTrue('builds' in response.context)
        self.assertEqual([build.pk for build in response.context['builds']], 2)
        build_1 = reponse.context['builds'][0]
        build_2 = response.context['builds'][1]
        self.assertGreaterThan(build_1.time, build_2.time)        


class TestBuilds(unittest.TestCase):
    '''
    Test to see if builds can be created user story 2 & 3
    '''
    fixtures = ['initial_data.json']

    def setUp(self):
        """setup function"""
        self.client = Client()
        self.driver = webdriver.Firefox()
        self.base_url = "http://127.0.0.1:8000/builds/new_build/"
        self.verificationErrors = []
 
    def test_sign_in(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_link_text("Login").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("waleed")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("waleed")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()


    def test_save_builds(self):
        '''
        Test if builds are saved
        '''    
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("waleed")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("waleed")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_id("name_input").click()
        driver.find_element_by_id("name_input").clear()
        driver.find_element_by_id("name_input").send_keys("Test name")
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
        driver.find_element_by_id("id_hdField").send_keys("hard drive")
        driver.find_element_by_name("access_right").click()
        Select(driver.find_element_by_name("access_right")).select_by_visible_text("Public")
        driver.find_element_link_by_text("Submit Query").click()       

    def tearDown(self):
        """delete models from test database"""
        self.driver.quit()
        self.assertEqual([], self.verificationErrors

class Test_Edit_Builds(unittest.TestCase):
    '''
    Test to see if build page is editable User Story 22
    '''
    fixtures = ['initial_data.json']

    def setUp(self):
        """setup function"""
        self.client = Client()
        self.driver = webdriver.Firefox()
        self.base_url = "http://127.0.0.1:8000/builds/edit_build/First__Build/"
        self.verificationErrors = []

    def test_edit_builds(self):
        '''
        Test if builds are editable
        '''    
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("waleed")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("waleed")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_id("name_input").click()
        driver.find_element_by_id("name_input").clear()
        driver.find_element_by_id("name_input").send_keys("Test name after Editing")
        driver.find_element_by_id("id_moboField").click()
        driver.find_element_by_id("id_moboField").clear()
        driver.find_element_by_id("id_moboField").send_keys("motherboard 2")
        driver.find_element_by_id("id_cpuField").click()
        driver.find_element_by_id("id_cpuField").clear()
        driver.find_element_by_id("id_cpuField").send_keys("processor 2")
        driver.find_element_by_id("id_gpuField").click()
        driver.find_element_by_id("id_gpuField").clear()
        driver.find_element_by_id("id_gpuField").send_keys("graphics 2")
        driver.find_element_by_id("id_caseField").click()
        driver.find_element_by_id("id_caseField").clear()
        driver.find_element_by_id("id_caseField").send_keys("case 2")
        driver.find_element_by_id("id_memField").click()
        driver.find_element_by_id("id_memField").clear()
        driver.find_element_by_id("id_memField").send_keys("memory 2")
        driver.find_element_by_id("id_hdField").click()
        driver.find_element_by_id("id_hdField").clear()
        driver.find_element_by_id("id_hdField").send_keys("hard drive 2")
        driver.find_element_by_name("access_right").click()
        Select(driver.find_element_by_name("access_right")).select_by_visible_text("Private")
        driver.find_element_link_by_text("Submit Query").click()       

    def tearDown(self):
        """delete models from test database"""
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

class DeleteBuild(unittest.TestCase):
    """
    Test to see if user can delete previous build User Story 23
    """
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = "http://127.0.0.1:8000/builds/edit/"
        self.verificationErrors = []
    
    def test_delete(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("waleed")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("waleed")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_link_text("Edit Build").click()
        driver.find_element_by_link_text("Delete").click()
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

class TestViewBuild(unittest.TestCase):
    """
    Test to see if user can view a build in detail User Story 18
    """
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = "http://127.0.0.1:8000/builds/home/"
        self.verificationErrors = []
    
    def test_read(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_link_text("View").click()
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

class TestRegistration(unittest.TestCase):
    """
    Test to see if user can test_register User Story 1
    """
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = "http://127.0.0.1:8000"
        self.verificationErrors = []

    def test_register(self):
        driver = self.driver
        driver.find_element_by_link_text("Sign In").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("user")
        driver.find_element_by_id("id_email").clear()
        driver.find_element_by_id("id_email").send_keys("waleed@gmail.com")
        driver.find_element_by_id("id_password1").clear()
        driver.find_element_by_id("id_password1").send_keys("password")
        driver.find_element_by_id("id_password2").clear()
        driver.find_element_by_id("id_password2").send_keys("password")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
       
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

class TestSetMaxCost(unittest.TestCase):
    """
    Test to see if user can set a max cost user story 7
    """

    def setUp(self):
        """setup function"""
        self.client = Client()
        self.driver = webdriver.Firefox()
        self.base_url = "http://127.0.0.1:8000/builds/new_build/cost/"
        self.verificationErrors = []
     
    
    def test_max_cost(self):
        """
        set the max cost of each part of build - User Story 7
        """
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_link_text("Set Max Cost Motherboard").click()
        Select(driver.find_element_by_name("Price")).select_by_visible_text("99.99")   
        driver.find_element_by_link_text("Set Max Cost Processor").click()
        Select(driver.find_element_by_name("Price")).select_by_visible_text("199.99") 
        driver.find_element_by_link_text("Set Max Cost Graphics Card").click()
        Select(driver.find_element_by_name("Price")).select_by_visible_text("49.99") 
        driver.find_element_by_link_text("Set Max Cost Memory").click()
        Select(driver.find_element_by_name("Price")).select_by_visible_text("99.99") 
        driver.find_element_by_link_text("Set Max Cost Hard Drive").click()
        Select(driver.find_element_by_name("Price")).select_by_visible_text("99.99") 
        driver.find_element_by_link_text("Set Max Cost Case").click()
        Select(driver.find_element_by_name("Price")).select_by_visible_text("99.99")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click() 

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)        

if __name__ ==  '__main__':
    unittest.main()

'''
    
    def test_builds(self):
        found = resolve('/builds/home/')
        self.assertEqual(found.func, new_build)
        
    def test_builds_html(self):
        request = HttpRequest()
        response = new_build(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>User Page</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
    

'''
