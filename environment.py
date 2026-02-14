from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def before_scenario(context, scenario):
    options = Options()
    options.add_argument("--start-maximized")
    context.driver = webdriver.Chrome(options=options)


def after_scenario(context, scenario):
    context.driver.quit()
