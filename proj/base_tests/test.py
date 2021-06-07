import pytest
from base_tests.base import BaseCase

from selenium.common.exceptions import TimeoutException

from ui.locators.pages_locators import LoginPageLocators


class TestOne(BaseCase):

    @pytest.mark.UI
    def test_login_negative1(self, login_page_negative):
        login_page_negative.credentials(login='InvalidLogin')
        assert login_page_negative.find(LoginPageLocators.INVALID_LOGIN)

    @pytest.mark.UI
    def test_login_negative2(self, login_page_negative):
        login_page_negative.credentials(login="CID22888WRONG@yandex.ru")
        assert 'account.my.com/login/?error_code' in self.driver.current_url

    @pytest.mark.UI
    def test_company_create(self, login_page):
        self.company_page.check_if_campaign_created()

    @pytest.mark.UI
    def test_audience(self, login_page):
        self.audience_page.check_if_audience_created()

    @pytest.mark.UI
    def test_audience_delete(self, login_page):
        self.audience_page.check_if_audience_created()

        with pytest.raises(TimeoutException):
            self.audience_page.check_if_audience_deleted()
