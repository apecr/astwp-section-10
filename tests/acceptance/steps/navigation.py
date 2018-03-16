from behave import *
from selenium import webdriver

use_step_matcher('re')

@given('I am on the home page')
def step_impl(context):
    browser = webdriver.Chrome()
    browser.get('http://127.0.0.1:5002/')



# Feature: Test navigation between pages
#   We can have a longer description that
#   can span a few lines
#
#   Scenario: Homepage can go to Blog
#     Given I am on the home page
#     When I clock on the link with id "blog-link"
#     Then I am on the blog page