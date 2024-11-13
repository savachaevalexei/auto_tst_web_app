import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_false_user(site, x_selector1, x_selector2, x_selector3, btn_selector, error1, false_user_data):
    input1 = site.find_element("xpath", x_selector1)
    input1.send_keys(false_user_data[0])

    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys(false_user_data[1])

    btn = site.find_element("css", btn_selector)
    btn.click()

    err_label = site.find_element("xpath", x_selector3)
    text = err_label.text
    assert text == error1  
    

def test_true_user(site, x_selector1, x_selector2, x_selector4, btn_selector, error2, true_user_data):
    input1 = site.find_element("xpath", x_selector1)
    input1.clear()
    input1.send_keys(true_user_data[0])

    input2 = site.find_element("xpath", x_selector2)
    input2.clear()
    input2.send_keys(true_user_data[1])

    btn = site.find_element("css", btn_selector)
    btn.click()

    user_label = site.find_element("xpath", x_selector4)
    text = user_label.text
    assert text == error2
    

def test_add_post(site, x_selector1, x_selector2, btn_selector, 
                  create_btn, post_title_input, post_description_input, 
                  post_content_input, post_save_btn, post_title_selector, 
                  time_wait, post_data):
    
    create_post_btn = site.find_element("css", create_btn)
    create_post_btn.click()
    time.sleep(time_wait)

    title_input = site.find_element("xpath", post_title_input)
    title_input.send_keys(post_data[0])

    description_input = site.find_element("xpath", post_description_input)
    description_input.send_keys(post_data[1])

    content_input = site.find_element("xpath", post_content_input)
    content_input.send_keys(post_data[2])
    time.sleep(time_wait)

    wait = WebDriverWait(site.driver, 10)
    save_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, post_save_btn)))
    save_button.click()

    saved_post_title = wait.until(
        EC.presence_of_element_located((By.XPATH, f"//h1[text()='{post_data[0]}']"))
    )

    post_title_element = site.find_element("xpath", post_title_selector)
    assert post_title_element.text == post_data[0]