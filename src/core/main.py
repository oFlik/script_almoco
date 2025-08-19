from ..config.basic_info import FORM_LINK, divisions
from ..config.driver_config import config_webdriver
from ..config.database import get_div_data
from .filler import fill_form


def start_filler():
    ask_to_skip = True
    for division in divisions:

        try:
            d_data = get_div_data(division)

            if d_data[1] == 0:
                print(f'''Divisão {
                      division} não possui funcionários para almoçar''')
                continue

            if ask_to_skip == True:
                skip = input(f'Divisão: {division}. Pular? S ou N: ')

                if skip == 'N' or skip == 'n':
                    ask_to_skip = False
                elif skip == 'S' or skip == 's':
                    continue

            browser = config_webdriver()
            browser.get(FORM_LINK)

            fill_form(browser, division, d_data)
        except Exception as int_err:
            print(f"Algo deu errado: {int_err}")
            break

        browser.close()
