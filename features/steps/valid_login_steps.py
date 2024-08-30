import time

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('the browser is launched')
def launch_browser(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(3)

@when('the user enters a valid username and password')
def enter_credentials(context):

    WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[name="username"]'))).send_keys("Admin")
    WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[name="password"]'))).send_keys("admin123")


@when('the user clicks the login button')
def click_login(context):
    WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[type="submit"]'))).click()


@then('the user should be successfully logged in')
def verify_login(context):
    time.sleep(3)
    verify_text = context.driver.find_element(By.CSS_SELECTOR, '.oxd-topbar-header-breadcrumb>h6').text
    assert 'Dashboard' in verify_text

