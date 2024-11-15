from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging, yaml

class TestSearchLocators:
    ids = dict()
    with open ("./locators.yaml") as f:
        locators = yaml.safe_load(f)
        
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])
    
 
class OperationsHelperUI(BasePage):
    
    def enter_text_info_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send {word} to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not Found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operation with {locator}")
            return False
        return True
    
    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception with click")
            return False
        logging.debug(f"Clicked {element_name} button")
        return True
    
    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while text from {element_name}")
            return None
        logging.debug(f"We find text {text} in field {element_name}")
        return text
    
    # ENTER ENTER ENTER ENTER ENTER ENTER ENTER ENTER ENTER ENTER ENTER ENTER ENTER ENTER ENTER ENTER ENTER ENTER
    
    # Ввод логина
    def enter_login(self, word):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"], word, description="login form")
        
    # Ввод пароля    
    def enter_pass(self, word):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_PASS_FIELD"], word, description="password form")

     # Ввод названия поста   
    def enter_post_title(self, word):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_FORM_POST_TITLE_FIELD"], word, description="post_title form")

    # Ввод описания поста   
    def enter_post_description(self, word):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_FORM_POST_DESCRIPTION_FIELD"], word, description="LOCATOR_FORM_POST_DESCRIPTION_FIELD form")

    # Ввод содержания поста   
    def enter_post_content(self, word):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_FORM_POST_CONTENT_FIELD"], word, description="LOCATOR_FORM_POST_CONTENT_FIELD")
        
    # Ввод в контактную форму - имя
    def enter_name_to_contact_form(self, word):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_CONTACT_LOGIN_FIELD"], word, description="LOCATOR_CONTACT_LOGIN_FIELD")

    # Ввод в контактную форму - почта
    def enter_email_to_contact_form(self, word):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_CONTACT_EMAIL_FIELD"], word, description="LOCATOR_CONTACT_EMAIL_FIELD")
        
    # Ввод в контактную форму - контакт
    def enter_content_to_contact_form(self, word):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_CONTACT_CONTENT_FIELD"], word, description="LOCATOR_CONTACT_CONTENT_FIELD")
        
    # CLICK CLICK CLICK CLICK CLICK CLICK CLICK CLICK CLICK CLICK CLICK CLICK CLICK CLICK CLICK CLICK
    
     # Нажатие на кнопку создание нового поста   
    def click_create_new_post_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CREATE_NEW_POST_BUTTON"], description="LOCATOR_CREATE_NEW_POST_BUTTON")
    
    # Нажатие на кнопку сохранить пост   
    def click_save_post_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_SAVE_POST_BUTTON"], description="LOCATOR_SAVE_POST_BUTTON")

     # Нажатие на ссылку Contact
    def click_contact_link(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CLICK_CONTACT_LINK"], description="LOCATOR_CLICK_CONTACT_LINK")

    # Нажатие на кнопку contact_us
    def click_contact_us_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_US_BUTTON"], description="LOCATOR_CONTACT_US_BUTTON")
              
    # Нажатие на кнопку авторизации  
    def click_login_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_LOGIN_BTN"], description="LOCATOR_LOGIN_BTN")

    # GET GET GET GET GET GET GET GET GET GET GET GET GET GET GET GET GET GET GET GET GET GET 
        
    # Получение сообщения об ошибке    
    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_ERROR_FIELD"], description="LOCATOR_ERROR_FIELD")
    
    # Получение имени авторизованного пользователя
    def get_user_login_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_USER_NAME_FIELD"], description="LOCATOR_USER_NAME_FIELD")

    # Получение названия поста  
    def get_post_title_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_POST_TITLE_FIELD"], description="LOCATOR_ERROR_FIELD")

    # Получение текста 
    def get_contact_us_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_CONTACT_US_TEXT"], description="LOCATOR_CONTACT_US_TEXT")

    def get_alert(self):
        logging.info("Get Alert text")
        text = self.get_alert_text()
        logging.info(text)
        return text

    
    