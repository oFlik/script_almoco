from selenium import webdriver


def config_webdriver():
    chr_options = webdriver.ChromeOptions()

    chr_options.add_argument("--log-level=0")
    chr_options.add_argument("--log-level=1")
    chr_options.add_experimental_option("excludeSwitches", ["enable-logging"])

    browser = webdriver.Chrome(options=chr_options)

    return browser
