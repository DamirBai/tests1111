from os import getenv
from selenium import webdriver

WAIT_SECONDS = int(getenv('WAIT_SECONDS', '30'))
BASE_URL = getenv('BASE_URL', 'http://localhost:8080')
DRIVER = getenv('DRIVER', 'firefox').lower()


def before_all(context):
    context.base_url = BASE_URL
    context.wait_seconds = WAIT_SECONDS
    if 'firefox' in DRIVER:
        context.driver = get_firefox()
    else:
        context.driver = get_chrome()
    context.driver.implicitly_wait(context.wait_seconds)
    context.config.setup_logging()


def after_all(context):
    context.driver.quit()


def get_chrome():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    return webdriver.Chrome(options=options)


def get_firefox():
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    return webdriver.Firefox(options=options)
