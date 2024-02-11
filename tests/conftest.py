import pytest
from selene.support.shared import browser


@pytest.fixture(autouse=True)
def settings():
    browser.config.window_height, browser.config.window_width = 1920, 1080
    browser.config.base_url = 'https://github.com/'
    browser.config.timeout = 5
    yield
    browser.quit()
