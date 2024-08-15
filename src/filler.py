import time
from .config.basic_info import WAIT_TIME, NAME, option_paths
from .question_types import fill_text, fill_dropdown, fill_with_click


def fill_form(b, d_name, d_data):
    employees_count = d_data[1]
    option_number = d_data[2]

    print(f"Iniciando preenchimento do formulário || Setor: {d_name}")
    print(f"Quantidade de refeições: {employees_count}")

    time.sleep(WAIT_TIME)

    fill_text(b, option_paths["namefield"], NAME)
    print("Nome .............. Ok")

    time.sleep(WAIT_TIME)

    checkboxes = [option_paths["company_checkbox"], option_paths["department_checkbox"]]

    for x, box in enumerate(checkboxes):
        fill_with_click(b, box)
        print("Empresa" if x == 1 else "Setor  ", "........... Ok")

        time.sleep(WAIT_TIME)

    fill_text(b, option_paths["quantity_field"], employees_count)
    print("Quantidade ........ Ok")

    time.sleep(WAIT_TIME)

    fill_dropdown(b, option_paths["divisions_dropbox"], option_number)
    print("Centro de Custo ... Ok")

    safety_stop = input('Continuar? ("s" ou "n"): ')

    if safety_stop != "s":
        raise InterruptedError("Saída solicitada")

    time.sleep(WAIT_TIME)

    fill_with_click(b, option_paths["submit"])
    print(f"Envio completo. || Setor: {d_name}")
    print()

    time.sleep(WAIT_TIME)
    return
