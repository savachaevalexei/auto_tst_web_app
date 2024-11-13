import yaml
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


with open("test_data.yaml") as f:
    test_data = yaml.safe_load(f)
   


class Site:
    def __init__(self, address, browser):
        if browser == "firefox":
            service = FirefoxService(executable_path=GeckoDriverManager().install())
            options = webdriver.FirefoxOptions()
            self.driver = webdriver.Firefox(service=service, options=options)
        elif browser == "chrome":
            service = ChromeService(executable_path=ChromeDriverManager().install())
            options = webdriver.ChromeOptions()
            self.driver = webdriver.Chrome(service=service, options=options)
            
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.driver.get(address)
        time.sleep(test_data["sleep_time"])
        
    
    def find_element(self, mode, path):
        if mode == "css":
            element = self.driver.find_element(By.CSS_SELECTOR, path)
        elif mode == "xpath":
            element = self.driver.find_element(By.XPATH, path)
        else:
            None
        return element
    
    
    def get_element_property(self, mode, path, property):
        element = self.find_element(mode, path)
        return element.value_of_css_property(property)
    
    
    def close(self):
        self.driver.close()
        
    
    def quit(self):
        self.driver.quit()
        
