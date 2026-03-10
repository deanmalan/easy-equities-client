import os
import csv

dir_path = os.path.dirname(os.path.realpath(__file__))
currencies_file = f"{dir_path}/currencies.csv"


def convert_non_ascii_currency_symbol_to_ascii_code(symbol: str) -> str | None:
    """
    XXX: Imperfect, because $, for example, will always convert to USD.
    """

    with open(currencies_file, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["symbol"] == symbol:
                return row["code"]
