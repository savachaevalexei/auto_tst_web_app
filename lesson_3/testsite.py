from BaseApp import BasePage

from selenium.webdriver.common.by import By
import logging

class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, "button")
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_USER_NAME_FIELD = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[3]""")
    LOCATOR_CREATE_NEW_POST_BUTTON = (By.XPATH, """//*[@id="create-btn"]""")
    
    LOCATOR_FORM_POST_TITLE_FIELD = (By.XPATH, """//*[@id='create-item']/div/div/div[1]/div/label/input""")
    LOCATOR_FORM_POST_DESCRIPTION_FIELD = (By.XPATH, """//*[@id='create-item']/div/div/div[2]/div/label/span/textarea""")
    LOCATOR_FORM_POST_CONTENT_FIELD = (By.XPATH, """//*[@id='create-item']/div/div/div[3]/div/label/span/textarea""")
    LOCATOR_SAVE_POST_BUTTON = (By.XPATH, """/html/body/div/main/div/div/form/div/div/div[7]/div/button""")
    
    LOCATOR_POST_TITLE_FIELD = (By.XPATH, """/html/body/div[1]/main/div/div[1]/h1""")
    
    LOCATOR_CLICK_CONTACT_LINK = (By.XPATH, """/html/body/div[1]/main/nav/ul/li[2]/a""")
    LOCATOR_CONTACT_US_TEXT = (By.XPATH, """/html/body/div[1]/main/div/div/h1""")
    
    LOCATOR_CONTACT_LOGIN_FIELD = (By.XPATH, """/html/body/div[1]/main/div/div/form/div[1]/label/input""")
    LOCATOR_CONTACT_EMAIL_FIELD = (By.XPATH, """/html/body/div[1]/main/div/div/form/div[2]/label/input""")
    LOCATOR_CONTACT_CONTENT_FIELD = (By.XPATH, """/html/body/div[1]/main/div/div/form/div[3]/label/span/textarea""")
    LOCATOR_CONTACT_US_BUTTON = (By.XPATH, """/html/body/div[1]/main/div/div/form/div[4]/button""")
    
    
    
class OperationsHelper(BasePage):
    # Ввод логина
    def enter_login(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)
        
    # Ввод пароля    
    def enter_pass(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)
        
    # Нажатие на кнопку авторизации  
    def click_login_button(self):
        logging.info("Click login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()
    
    # Получение сообщения об ошибке    
    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=3)
        text = error_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        return text
    
    # Получение имени авторизованного пользователя
    def get_user_login_text(self):
        user_login_field = self.find_element(TestSearchLocators.LOCATOR_USER_NAME_FIELD, time=3)
        text = user_login_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_USER_NAME_FIELD[1]}")
        return text
    
    # Нажатие на кнопку создание нового поста   
    def click_create_new_post_button(self):
        logging.info("Click CREATE_NEW_POST_BUTTON")
        self.find_element(TestSearchLocators.LOCATOR_CREATE_NEW_POST_BUTTON).click()
    
    # Ввод названия поста   
    def enter_post_title(self, word):
        login_field = self.find_element(TestSearchLocators.LOCATOR_FORM_POST_TITLE_FIELD)
        login_field.clear()
        login_field.send_keys(word)
    
    # Ввод описания поста   
    def enter_post_description(self, word):
        login_field = self.find_element(TestSearchLocators.LOCATOR_FORM_POST_DESCRIPTION_FIELD)
        login_field.clear()
        login_field.send_keys(word)
    
    # Ввод содержания поста   
    def enter_post_content(self, word):
        login_field = self.find_element(TestSearchLocators.LOCATOR_FORM_POST_CONTENT_FIELD)
        login_field.clear()
        login_field.send_keys(word)
    
    # Нажатие на кнопку сохранить пост   
    def click_save_post_button(self):
        logging.info("Click LOCATOR_SAVE_POST_BUTTON")
        self.find_element(TestSearchLocators.LOCATOR_SAVE_POST_BUTTON).click()
    
    # Получение названия поста  
    def get_post_title_text(self):
        post_title_text = self.find_element(TestSearchLocators.LOCATOR_POST_TITLE_FIELD, time=3)
        text = post_title_text.text
        return text
    
    # Нажатие на ссылку Contact
    def click_contact_link(self):
        logging.info("Click LOCATOR_CLICK_CONTACT_LINK")
        self.find_element(TestSearchLocators.LOCATOR_CLICK_CONTACT_LINK).click()
        
    # Проверка что попали на страницу с формой обратной связи
    def get_contact_us_text(self):
        contact_us_text = self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_TEXT, time=3)
        text = contact_us_text.text
        return text
    
    # Ввод в контактную форму - имя
    def enter_name_to_contact_form(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_CONTACT_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)
        
    # Ввод в контактную форму - почта
    def enter_email_to_contact_form(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_CONTACT_EMAIL_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_EMAIL_FIELD)
        login_field.clear()
        login_field.send_keys(word)
        
    # Ввод в контактную форму - контакт
    def enter_content_to_contact_form(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_CONTACT_CONTENT_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_CONTENT_FIELD)
        login_field.clear()
        login_field.send_keys(word)
        
    
    # Нажатие на кнопку contact_us
    def click_contact_us_button(self):
        logging.info("Click LOCATOR_CONTACT_US_BUTTON")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_BUTTON).click()
        
    
    # Проверка alert_text 
    def check_alert_text(self):
        alert = self.driver.switch_to.alert
        text = alert.text 
        return text
    


    
    