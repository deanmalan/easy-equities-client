"""
Download all of your transactions for the last year in JSON format.

This method contains more information on the transaction, but EasyEquities
only allows one year worth of data to be downloaded from it. See
examples/get_transactions_for_period.py for a way to download more years
of data, but with less detailed data.

Usage: uv run examples/get_transactions_year.py
"""

import json
import os

from easy_equities_client.clients import (
    EasyEquitiesClient,
    PlatformClient,
    SatrixClient,
)

platform = "easyequities"
username = os.environ["EE_USERNAME"]
password = os.environ["EE_PASSWORD"]

client: PlatformClient = (
    EasyEquitiesClient() if platform == "easyequities" else SatrixClient()
)
client.login(username=username, password=password)

accounts = client.accounts.list()

if not os.path.exists("output"):
    os.makedirs("output")

for account in accounts:
    print(f"Getting transactions for account {account.id}. ")
    transactions = client.accounts.transactions(account.id)

    file_name = f"output/year_transactions_{account.id}.json"

    print(f"Saving to {file_name}")

    with open(file_name, "w") as f:
        f.write(json.dumps(transactions, indent=4))
