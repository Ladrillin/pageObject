import time

from ui.pages.base_page import BasePage
from ui.locators.pages_locators import AudienceLocators


class AudiencePage(BasePage):

    locators = AudienceLocators
    audience_title = str(time.time()) + 'AUDIENCE_TITLE'

    def create_audience(self, audience_title):
        self.click_on_element(AudienceLocators.AUDIENCE_CATEGORY)
        self.click_on_element(AudienceLocators.SPAN_MENU)
        self.click_on_element(AudienceLocators.PAY_CHECKBOX)
        self.click_on_element(AudienceLocators.ADD_SEGMENT)

        self.send_keys_to_input(AudienceLocators.TITLE_INPUT, audience_title)
        self.click_on_element(AudienceLocators.CREATE_SEGMENT)

    def delete_audience(self, audience_title):
        title_checkbox_locator = self.locators().audience_title_checkbox_locator(audience_title)
        self.click_on_element(title_checkbox_locator)
        self.click_on_element(AudienceLocators.ACTION_CAROUSEL)
        self.click_on_element(AudienceLocators.CAROUSEL_DELETE_BUTTON)

    def check_if_audience_created(self):
        self.driver.get('https://target.my.com/segments/segments_list/new')
        self.create_audience(self.audience_title)

        self.find(self.locators().audience_title_locator(self.audience_title))

        self.delete_audience(self.audience_title)

    def check_if_audience_deleted(self):
        self.find(self.locators().audience_title_locator(self.audience_title))


