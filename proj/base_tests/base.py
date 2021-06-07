import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.company_page import CompanyPage
from ui.pages.audience_page import AudiencePage


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.company_page: CompanyPage = request.getfixturevalue('company_page')
        self.audience_page: AudiencePage = request.getfixturevalue('audience_page')
