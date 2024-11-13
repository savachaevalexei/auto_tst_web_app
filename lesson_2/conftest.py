import pytest
import yaml
from module import Site


with open("test_data.yaml") as f:
    test_data = yaml.safe_load(f)
    
name = test_data.get("username")

@pytest.fixture(scope="module")
def site():
    site_instance = Site(test_data["address"], test_data["browser"])
    yield site_instance
    site_instance.quit()
 
@pytest.fixture()
def time_wait():
    wait = test_data.get("wait")
    return wait
     
@pytest.fixture()
def false_user_data():
    name = "name"
    passw = "passw"
    return name, passw

@pytest.fixture()
def true_user_data():
    name = test_data.get("username")
    passw = test_data.get("password")
    return name, passw

@pytest.fixture()
def x_selector1():
    return """//*[@id="login"]/div[1]/label/input"""

@pytest.fixture()
def x_selector2():
    return """//*[@id="login"]/div[2]/label/input"""

@pytest.fixture()
def x_selector3():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""

@pytest.fixture()
def x_selector4():
    return """//*[@id="app"]/main/nav/ul/li[3]/a"""

@pytest.fixture()
def btn_selector():
    return "button"

@pytest.fixture()
def error1():
    return "401"

@pytest.fixture()
def error2():
    return "Hello, {}".format(name)

@pytest.fixture()
def create_btn():
    return "#create-btn"

@pytest.fixture()
def post_title_input():
    return """//*[@id='create-item']/div/div/div[1]/div/label/input"""

@pytest.fixture()
def post_description_input():
    return """//*[@id='create-item']/div/div/div[2]/div/label/span/textarea"""

@pytest.fixture()
def post_content_input():
    return """//*[@id='create-item']/div/div/div[3]/div/label/span/textarea"""

@pytest.fixture()
def post_save_btn():
    return """button[type="submit"]"""

@pytest.fixture()
def post_title_selector():
    return """//*[@id='app']/main/div/div[1]/h1"""

@pytest.fixture()
def post_data():
    title = test_data.get("post_title")
    description = test_data.get("post_description")
    content = test_data.get("post_content")
    return title, description, content