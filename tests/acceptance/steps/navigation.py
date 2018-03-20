from behave import *
from selenium import webdriver
from unittest import TestCase
from tests.acceptance.page_model.blog_page import BlogPage
from tests.acceptance.page_model.home_page import HomePage

use_step_matcher('re')
tc = TestCase('__init__')
blog_page = BlogPage(webdriver.Chrome())
home_page = HomePage(webdriver.Chrome())


@given('I am on the home page')
def step_impl(context):
    context.driver = blog_page.driver
    context.driver.get(home_page.url)


@then('I am on the blog page')
def step_impl(context):
    tc.assertEqual(blog_page.url, context.driver.current_url)


@given("I am on the blog page")
def step_impl(context):
    context.driver = blog_page.driver
    context.driver.get(blog_page.url)


@then("I am on the home page")
def step_impl(context):
    tc.assertEqual(home_page.url, context.driver.current_url)
