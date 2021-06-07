from selenium.webdriver.common.by import By


class LoginPageLocators:
    HEADER_BUTTON = (By.XPATH, '//div[text()="Войти"]')
    LOGIN_INPUT = (By.CSS_SELECTOR, '[name="email"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[name="password"]')
    LOGIN_BUTTON = (By.XPATH, '//div[contains(@class, "authForm-module-button")]')
    INVALID_LOGIN = (By.XPATH, '//div[text()="Введите email или телефон"]')


class BasesPageLocators:
    HEADER_BUTTON = (By.XPATH, '//div[text()="Войти"]')


class CompanyLocators:

    CREATE_COMPANY = (By.XPATH, '//div[text()="Создать кампанию"]')
    COMPANY_TYPE_BUTTON = (By.XPATH, '//div[text()="Трафик"]')
    INPUT_URL = (By.XPATH, '//input[@data-gtm-id="ad_url_text"]')
    ADV_TYPE = (By.XPATH, '//span[text()="Баннер"]')  # Нужен скролл

    IMAGE_UPLOAD_INPUT = (By.XPATH, '//input[@data-test="image_240x400"]')  # Нужен скролл
    IMAGE_UPLOAD_BUTTON = (By.XPATH, '//div[@data-test="button"]/div[text()="240 × 400"]')
    SAVE_UPLOADED_IMAGE = (By.XPATH, '//input[@value="Сохранить изображение"]')

    TITLE_INPUT = (By.XPATH, '//div[@data-class-name="Input"]/div/input[@maxlength="255"]')

    TITLE_TEMPLATE = '//a[text()="{}"]'
    TITLE_CHECKBOX_TEMPLATE = '//a[text()="{}"]/preceding-sibling::input[@type="checkbox"]'

    def campaign_title_locator(self, campaign_title):
        return By.XPATH, self.TITLE_TEMPLATE.format(campaign_title)

    def campaign_title_checkbox_locator(self, campaign_title):
        return By.XPATH, self.TITLE_CHECKBOX_TEMPLATE.format(campaign_title)

    ACTION_CAROUSEL = (By.XPATH, '//span[text()="Действия"]')
    DELETE_BUTTON = (By.XPATH, '//li[text()="Удалить"]')


class AudienceLocators:
    HEADER_LINK_BUTTON = (By.XPATH, '//a[@href="/segments"]')

    CREATE_BUTTON = (By.XPATH, '//a[@href="/segments/segments_list/new/"]')

    AUDIENCE_CATEGORY = (By.XPATH, '//div[text()="Приложения и игры в соцсетях"]')
    SPAN_MENU = (By.XPATH, '//span[text()="Игравшие и платившие в платформе"]')
    PAY_CHECKBOX = (By.XPATH, '//input[@value="pay"]')
    ADD_SEGMENT = (By.XPATH, '//div[text()="Добавить сегмент"]')

    TITLE_INPUT = (By.XPATH, '//input[@maxlength="60"]')
    CREATE_SEGMENT = (By.XPATH, '//div[text()="Создать сегмент"]')

    AUDIENCE_TITLE_TEMPLATE = '//a[@title="{}"]'
    AUDIENCE_TITLE_CHECKBOX_TEMPLATE = '//a[text()="{}"]//preceding::input[@type="checkbox"][1]'

    def audience_title_locator(self, audience_title):
        return By.XPATH, self.AUDIENCE_TITLE_TEMPLATE.format(audience_title)

    def audience_title_checkbox_locator(self, audience_title):
        return By.XPATH, self.AUDIENCE_TITLE_CHECKBOX_TEMPLATE.format(audience_title)

    ACTION_CAROUSEL = (By.XPATH, '//span[text()="Действия"]')
    CAROUSEL_DELETE_BUTTON = (By.XPATH, '//li[text()="Удалить"]')

