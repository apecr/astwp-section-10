from behave import *

from tests.acceptance.page_model.base_page import BasePage

use_step_matcher('re')


@when('I clock on the "(.*)" link')
def step_impl(context, link_text):
    page = BasePage(context.driver)
    links = page.navigation
    matching_links = [l for l in links if l.text == link_text]
    if len(matching_links) > 0:
        matching_links[0].click()
    else:
        raise RuntimeError('The {} link does not exist'.format(link_text))