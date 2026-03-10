"""
Download all of your transactions for a given period in JSON format.

Usage: uv run examples/get_transactions_for_period.py
"""

import json
import os
from datetime import date, timedelta

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
    print(f"Getting transactions for account {account.id}")
    transactions = []
    end_date = date.today()
    start_date = end_date - timedelta(days=30)

    transactions = client.accounts.transactions_for_period(
        account.id, start_date, end_date
    )

    file_name = f"output/transactions_{account.id}.json"

    print(f"Saving to {file_name}")
    with open(file_name, "w") as f:
        f.write(json.dumps(transactions, indent=4))
