import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from ui.pages.login_page import LoginPage
from ui.pages.company_page import CompanyPage
from ui.pages.audience_page import AudiencePage


@pytest.fixture(scope='function')
def driver(config):
    url = config['url']
    manager = ChromeDriverManager(version='latest')
    browser = webdriver.Chrome(executable_path=manager.install())
    browser.maximize_window()
    browser.get(url)
    yield browser
    browser.quit()


@pytest.fixture(scope='function')
def login_page_negative(driver):
    return LoginPage(driver=driver)


@pytest.fixture(scope='function')
def login_page(driver):
    return LoginPage(driver=driver).credentials()


@pytest.fixture
def company_page(driver):
    return CompanyPage(driver=driver)


@pytest.fixture
def audience_page(driver):
    return AudiencePage(driver=driver)
