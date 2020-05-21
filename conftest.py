import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Specify a language: ru, es, fr, etc.. Default: ru")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    print("\nstart browser for test with language option '{}'..".format(language))
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()
