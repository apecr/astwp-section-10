from behave import *
from selenium import webdriver
from unittest import TestCase

use_step_matcher('re')
tc = TestCase('__init__')


@given('I am on the home page')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get('http://127.0.0.1:5002/')


@then('I am on the blog page')
def step_impl(context):
    expected_url = 'http://127.0.0.1:5002/blog'
    tc.assertEqual(expected_url, context.browser.current_url)


@given("I am on the blog page")
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get('http://127.0.0.1:5002/blog')


@then("I am on the home page")
def step_impl(context):
    expected_url = 'http://127.0.0.1:5002/'
    tc.assertEqual(expected_url, context.browser.current_url)
