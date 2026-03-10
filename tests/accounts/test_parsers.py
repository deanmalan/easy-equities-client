import pytest
from bs4 import BeautifulSoup

from easy_equities_client.accounts.parsers import (
    AccountOverviewParser,
    extract_account_info,
    get_amount_and_currency_from_string,
)
from easy_equities_client.accounts.types import Account


@pytest.fixture
def account_overview_div():
    contents = """
    <div style="background-color: #ed1747" class="selector-tabs active-tab"
        data-id="1000" data-tradingcurrencyid="1" data-tradingcurrencycolour="#ed1747"
        id="selector-tab">
        <div class="" id="trust-account-types">EasyEquities Test</div>
        <div class="funds-to-invest">
            <div class="white">Funds to invest:</div>
            <div class="white bold-heavy"><span>R5.00</span></div>
        </div>
    </div>
    """
    return BeautifulSoup(contents, "html.parser").div.div


def test_extract_account_info(account_overview_div):
    assert Account(
        name="EasyEquities Test", trading_currency_id="1", id="1000"
    ) == extract_account_info(account_overview_div)


class TestAccountOverviewParser:
    def test_account_overview_parser(self, account_overview_page):
        parser = AccountOverviewParser(account_overview_page)
        expected_result = [
            Account(id="1000", name="EasyEquities ZAR", trading_currency_id="2"),
            Account(id="2000", name="TFSA", trading_currency_id="3"),
            Account(
                id="3000",
                name="EasyEquities USD",
                trading_currency_id="10",
            ),
            Account(
                id="4000",
                name="EasyEquities AUD",
                trading_currency_id="16",
            ),
        ]
        assert expected_result == parser.extract_accounts()


@pytest.mark.parametrize(
    (
        "amount_str",
        "expected_currency_symbol",
        "expected_currency_code",
        "expected_value",
    ),
    [
        ("R72.10", "R", "ZAR", 72.10),
        ("R14 433.48", "R", "ZAR", 14_433.48),
        ("-$0.11", "$", "USD", -0.11),
        ("€235.69", "€", "EUR", 235.69),
    ],
)
def test_get_amount_and_currency_from_string(
    amount_str: str,
    expected_currency_symbol: str,
    expected_currency_code: str,
    expected_value: float,
):
    currency_symbol, currency_code, value = get_amount_and_currency_from_string(
        amount_str
    )
    assert currency_symbol == expected_currency_symbol
    assert currency_code == expected_currency_code
    assert value == expected_value
