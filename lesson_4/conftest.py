import yaml, pytest, requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="session")
def browser():
    if browser == "firefox":
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = ChromeService(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()
    
with open("./test_data.yaml") as f:
    data = yaml.safe_load(f)

@pytest.fixture()
def login():
    res = requests.post(data["address"] + "gateway/login", data={"username": data["username"], "password": data["password"]})
    return res.json()["token"]

@pytest.fixture()
def testtext1():
    return "Заголовок поста"

@pytest.fixture()
def post_data():
    return {
        "title": "Заголовок поста",
        "description": "Описание поста",
        "content": "Содержание поста"
    }

@pytest.fixture()
def created_post(login, post_data):
    header = {"X-Auth-Token": login}
    res = requests.post(data["address"] + "api/posts", headers=header, data=post_data)
    assert res.status_code == 200
    return post_data