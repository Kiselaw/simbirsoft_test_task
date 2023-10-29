import pytest
from selenium import webdriver

@pytest.mark.parametrize("driver", ['chrome', 'firefox', 'edge'], indirect=True)
@pytest.fixture(scope="module")
def driver(request):
    """Создает driver с необходимыми настройками в зависимости от переданных аргументов"""
    browser = request.param
    options = {
        "firefox": webdriver.FirefoxOptions(),
        "chrome": webdriver.ChromeOptions(),
        "edge": webdriver.EdgeOptions(),
    }[browser]
    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        options=options
    )
    yield driver
    driver.quit()
