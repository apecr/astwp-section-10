Feature: Test navigation between pages
  We can have a longer description that
  can span a few lines

  Scenario: Homepage can go to Blog
    Given I am on the home page
    When I clock on the link with id "blog-link"
    Then I am on the blog page

  Scenario: Blog can go to homepage
    Given I am on the blog page
    When I clock on the link with id "home-link"
    Then I am on the home page