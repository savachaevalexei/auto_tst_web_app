from testsite import OperationsHelperUI
import logging, time


# Проверка авторизации с неверной парой логин-пароль
def test_false_user(browser):
    logging.info("test_false_user Starting")
    testpage = OperationsHelperUI(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("pass")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"
    
    
# Проверка авторизации валидной парой логин-пароль
def test_true_user(browser):
    logging.info("test_true_user Starting")
    testpage = OperationsHelperUI(browser)
    testpage.enter_login("alexxxxx")
    testpage.enter_pass("ad0364a494")
    testpage.click_login_button()
    assert testpage.get_user_login_text() == "Hello, alexxxxx"


# Проверка функции добавления поста
def test_add_post(browser):
    testpage = OperationsHelperUI(browser)
    testpage.click_create_new_post_button()
    time.sleep(3)
    title = "TITLE"
    testpage.enter_post_title(title)
    testpage.enter_post_description("DESCRIPTION")
    testpage.enter_post_content("CONTENT")
    testpage.click_save_post_button()
    time.sleep(3)
    assert testpage.get_post_title_text() == title
    
    
# Проверка ссылки на форму обратной связи
def test_contact_link(browser):
    testpage = OperationsHelperUI(browser)
    testpage.click_contact_link()
    time.sleep(3)
    assert testpage.get_contact_us_text() == "Contact us!"
    
    
# Проверка формы
def test_contact_form(browser):
    testpage = OperationsHelperUI(browser)
    testpage.enter_name_to_contact_form("NAME")
    testpage.enter_email_to_contact_form("ex@mail.ru")
    testpage.enter_content_to_contact_form("CONTENT")
    testpage.click_contact_us_button()
    time.sleep(3)
    assert testpage.get_alert() == "Form successfully submitted"