"""
TODO

Usage: uv run --with colorama examples/show_holdings_profit_loss.py <platform:satrix/easyequities> <username> <password>

"""

import sys

from easy_equities_client.clients import (
    EasyEquitiesClient,
    PlatformClient,
    SatrixClient,
)

if len(sys.argv) != 4:
    print(
        "Usage:\npython show_holdings_profit_loss.py <platform:satrix/easyequities> <username> <password>"
    )
    sys.exit()
platform = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]

client: PlatformClient = (
    EasyEquitiesClient() if platform == "easyequities" else SatrixClient()
)
client.login(username=username, password=password)

# List of accounts
accounts = client.accounts.list()
for account in accounts:
    print(f"{account.id}: {account.name}")

input_account_id = input(
    "Enter the account ID you'd like to generate a csv for: "
).strip()
selected_account = next(
    (account for account in accounts if account.id == input_account_id), None
)
if not selected_account:
    raise Exception("Invalid account selected")

transactions = client.accounts.transactions(selected_account.id)
