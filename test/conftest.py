import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import  Options

from helper.config import urlWeb

#def pytest_html_report_tittle(report): # fungsi nama report di html
#    report.tittle = "Report SindoNews Scope"

@pytest.fixture()
def openDriver():
    o = Options()
    o.add_argument("--headless")
    o.add_argument("--no-sandbox") #Bukan staging
    o.add_argument("--disable-dev-shm-usage")
    o.add_argument("--remote-allow-origins=*") #ini dapat di remote
    o.add_argument("--window-size=190,1080")
    o.add_argument("--disable-web-security")

    driver = webdriver.Chrome(options=o)
    driver.maximize_window()
    driver.implicitly_wait(15)
    return driver

@pytest.fixture(scope='function', autouse=True)
def hook(request, openDriver):
    openDriver.get(urlWeb)
    yield
    openDriver.quit()

@pytest.fixture(scope='session', autouse=True)
def suite(request):
    print("before test")
    yield
    print("after test")