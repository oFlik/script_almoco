from .config.basic_info import FORM_LINK, divisions
from .config.driver_config import config_webdriver
from .config.database import get_div_data
from .filler import fill_form


def start_filler():
    for division in divisions:
        try:
            browser = config_webdriver()
            browser.get(FORM_LINK)

            d_data = get_div_data(division)

            fill_form(browser, division, d_data)
        except Exception as int_err:
            print(f"Algo deu errado: {int_err}")
            break

        browser.close()
