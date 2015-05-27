from django.core.management import call_command
from django.test.simple import DjangoTestSuiteRunner

from lettuce import before, after, world
from logging import getLogger
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import re

logger = getLogger(__name__)
logger.info("Loading the terran file...")

@before.runserver
def setup_database(actual_server):
	'''
	This will setup your database, sync it, and run migrations if you are using South.
	It does this before the Test Django server is set up.
	'''
	logger.info("Setting up a test database...")
 
	# Uncomment if you are using South
	# patch_for_test_db_setup()
 
	world.test_runner = DjangoTestSuiteRunner(interactive=False)
	DjangoTestSuiteRunner.setup_test_environment(world.test_runner)
	world.created_db = DjangoTestSuiteRunner.setup_databases(world.test_runner)
 
	call_command('syncdb', interactive=False, verbosity=0)
 
	# Uncomment if you are using South
	# call_command('migrate', interactive=False, verbosity=0)

@after.runserver
def teardown_database(actual_server):
	'''
	This will destroy your test database after all of your tests have executed.
	'''
	logger.info("Destroying the test database ...")
 
	DjangoTestSuiteRunner.teardown_databases(world.test_runner, world.created_db)
 
@before.all
def setup_browser():
	world.browser = webdriver.PhantomJS()
	world.browser.set_window_size(1400,1000)

 
@after.all
def teardown_browser(total):
	world.browser.quit()


from lettuce import step

# Background
@step(u'I am at "([^"]*)"')
def i_am_at_url(step, url):
	logger.info("Go to the url: "+ url)
	world.browser.get(url)

# Steps
@step(u'I have title "([^"]*)" and content "([^"]*)"')
def i_have_title_and_test(step, title, content):
	logger.info("Save title and content in world")
	world.title = title
	world.content = content

@step(u'I put the data into the form and send form')
def put_data_in_form(step):
	logger.info("I will put the data in form and submit")
	title_input = world.browser.find_element_by_id('id_title')
	content_input = world.browser.find_element_by_id('id_content')
	submit = world.browser.find_element_by_id('create')

	if title_input is None:
		raise Exception("Title input not found")
	elif content_input is None:
		raise Exception("Sontent input not found")
	elif submit is None:
		raise Exception("Submit button not found")

	title_input.send_keys(world.title)
	content_input.send_keys(world.content)
	#raise()
	submit.click()
	#content_input.send_keys(Keys.RETURN)
	

@step(u'I should see "([^"]*)"')
def i_should_see(step, text):
	logger.info("Looking for the text")
	page = world.browser.page_source
	text_found = re.search(text, page)

	if text_found is None:
		raise Exception(page)

