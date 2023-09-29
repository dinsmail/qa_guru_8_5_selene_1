import pytest
from selene.support.shared import browser

@pytest.fixture(scope='function', autouse=True)
def open_browzer():

    # Открытие веб-страницы
    print("Открыть браузер и сайт")
    browser.open("https://demoqa.com/automation-practice-form")
    browser.config.window_width = 2880
    browser.config.window_height = 1800


    yield browser
    print("Закрыть все")
    browser.quit()