import pytest
import os
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.ie.service import Service as IEService
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType


@pytest.fixture()
def setup(browser):
    if browser.lower() == 'chrome':
        driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()))
        print("Launching Chrome browser......")
    elif browser.lower == 'firefox':
        driver = webdriver.Firefox(
            executable_path=GeckoDriverManager().install())
        print("Launching firefox browser......")
    elif browser.lower() == 'edge':
        driver = webdriver.Edge(service=EdgeService(
            EdgeChromiumDriverManager().install()))
        print("Launching Edge browser......")
    elif browser.lower() == 'ie':
        driver = webdriver.Ie(service=IEService(IEDriverManager().install()))
        print("Launching IE browser......")
    elif browser.lower() == 'chromium':
        driver = webdriver.Chrome(ChromeDriverManager(
            chrome_type=ChromeType.CHROMIUM).install())
        print("Launching chromium browser......")
    else:
        driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()))
        print("Defaulting to Launching Chrome browser.....")
    return driver


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # this will return the Browser value to setup method
    return request.config.getoption("--browser")


########## Pytest HTML Report ###########

# This is a hook for Adding Environment info to HTML Reports
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'ssatterf'


# This is a hook for delete/Modify Environment info to HTML Reports
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
