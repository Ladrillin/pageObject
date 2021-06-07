import time
import os
from selenium.webdriver.support import expected_conditions as EC

from ui.pages.base_page import BasePage
from ui.locators.pages_locators import CompanyLocators

BASE_TIMEOUT = 5


class CompanyPage(BasePage):

    locators = CompanyLocators()
    campaign_title = str(time.time()) + 'TEST_TITLE'

    def send_file(self, upload_locator, file_path, timeout=BASE_TIMEOUT):
        element = self.wait(timeout).until(EC.presence_of_element_located(upload_locator))
        element.send_keys(file_path)

    def clear_after_create(self, campaign_title):
        campaign_checkbox = CompanyLocators().campaign_title_checkbox_locator(campaign_title)
        self.click_on_element(campaign_checkbox)
        self.click_on_element(CompanyLocators.ACTION_CAROUSEL)
        self.click_on_element(CompanyLocators.DELETE_BUTTON)

    def create_campaign(self, campaign_title=str(time.time()) + 'TEST'):
        self.click_on_element(CompanyLocators.CREATE_COMPANY)

        self.click_on_element(CompanyLocators.COMPANY_TYPE_BUTTON)
        self.find(CompanyLocators.INPUT_URL)
        self.send_keys_to_input(CompanyLocators.INPUT_URL, 'http://vk.com/')

        self.scroll_to_elem(CompanyLocators.TITLE_INPUT)
        self.send_keys_to_input(CompanyLocators.TITLE_INPUT, campaign_title)

        self.scroll_to_elem(CompanyLocators.ADV_TYPE)
        self.click_on_element(CompanyLocators.ADV_TYPE)

        self.scroll_to_elem(CompanyLocators.IMAGE_UPLOAD_BUTTON)

        file_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(file_dir, 'image_for_upload.png')
        self.send_file(CompanyLocators.IMAGE_UPLOAD_INPUT, file_path)
        self.click_on_element(CompanyLocators.SAVE_UPLOADED_IMAGE)

        self.click_on_element(CompanyLocators.CREATE_COMPANY)

    def check_if_campaign_created(self):
        self.create_campaign(self.campaign_title)

        self.find(self.locators.campaign_title_locator(self.campaign_title))

        self.clear_after_create(self.campaign_title)


