import sys
from pathlib import Path
from sqlite3 import connect

db_path = Path(__file__).parents[2]

try:
    cursor = connect(f"{db_path}/fill_lunch.db")
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
