import sys
from sqlite3 import connect
from .basic_info import DB_PATH

try:
    cursor = connect(f"{DB_PATH}/fill_lunch.db")
except Exception:
    raise ConnectionError("Não foi possível conectar ao banco de dados")


def get_div_data(division):
    try:
        div_data = cursor.execute(f'SELECT * FROM divisions WHERE name = "{division}"')

        return div_data.fetchone()
    except Exception:
        raise ConnectionError("Erro na query")


if __name__ == "__main__":
    get_div_data(sys.argv[1])
