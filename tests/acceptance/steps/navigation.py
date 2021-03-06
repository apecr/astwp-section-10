from behave import *
from selenium import webdriver
from unittest import TestCase
from tests.acceptance.page_model.blog_page import BlogPage
from tests.acceptance.page_model.home_page import HomePage
from tests.acceptance.page_model.new_post_page import NewPostPage

use_step_matcher('re')
tc = TestCase('__init__')


@given('I am on the home page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    home_page = HomePage(context.driver)
    context.driver.get(home_page.url)


@then('I am on the blog page')
def step_impl(context):
    blog_page = BlogPage(context.driver)
    tc.assertEqual(blog_page.url, context.driver.current_url)


@given("I am on the blog page")
def step_impl(context):
    context.driver = webdriver.Chrome()
    blog_page = BlogPage(context.driver)
    context.driver.get(blog_page.url)


@then("I am on the home page")
def step_impl(context):
    home_page = HomePage(context.driver)
    tc.assertEqual(home_page.url, context.driver.current_url)


@given("I am on the new post page")
def step_impl(context):
    context.driver = webdriver.Chrome()
    new_post_page = NewPostPage(context.driver)
    context.driver.get(new_post_page.url)