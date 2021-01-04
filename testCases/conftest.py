from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path=r"C:\\Users\\bgh51998\\Downloads\\chromedriver_win32\\chromedriver.exe")
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=r"C:\\Users\\bgh51998\\Downloads\\geckodriver-v0.28.0-win64\\geckodriver.exe")
    else:
        driver = webdriver.Ie(executable_path=r"C:\\Users\\bgh51998\\Downloads\\IEDriverServer_x64_3.150.1\\IEDriverServer.exe")
    return driver


def pytest_addoption(parser): # this will get value from CLI
    parser.addoption('--browser')

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

####### Pytest HTML Report ###############
# It is hook for adding environmet info to HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['QA Resource'] = 'Rama'

# It is hook for delete/modify environment infor to HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins",None)
