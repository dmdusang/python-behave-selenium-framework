from behave import fixture, use_fixture
from framework import webapp

from selenium import webdriver
 from xvfbwrapper import Xvfb

def before_all(context):
 context.vdisplay = Xvfb()
 context.vdisplay.start()
 print("> Starting the browser")
 browser = context.config.userdata.get("browser")
 context.driver = webdriver.Firefox()

def after_all(context):
 print("< Closing the browser")
 context.driver.close()
 context.driver.quit()
 context.vdisplay.stop()
#def before_all(context):
    # -- SET LOG LEVEL: behave --logging-level=ERROR ...
    # on behave command-line or in "behave.ini".
   # context.config.setup_logging()

    # -- ALTERNATIVE: Setup logging with a configuration file.
    # context.config.setup_logging(configfile="behave_logging.ini")

#def after_all(context):