import pytest
from coinbase.rest import RESTClient
import markr


def test_init(MockCoinbase):
    assert isinstance(MockCoinbase, markr.exchanges.ExchangeBase)
    assert isinstance(MockCoinbase, markr.exchanges.Coinbase)
    assert isinstance(MockCoinbase.client, RESTClient)


def test_auth(MockCoinbase):
    assert MockCoinbase.client.is_authenticated


def test_get_price(MockCoinbase):
    assert hasattr(MockCoinbase, 'get_price') and callable(MockCoinbase.get_price)
    price = MockCoinbase.get_price(MockCoinbase.State.symbol)


def test_post_bid(MockCoinbase):
    assert hasattr(MockCoinbase, 'post_bid') and callable(MockCoinbase.post_bid)
    price = 100.
    order_str = f'Bidding {MockCoinbase.State.symbol} at {price}'
    assert order_str == MockCoinbase.post_bid(MockCoinbase.State.symbol, price)


def test_post_ask(MockCoinbase):
    assert hasattr(MockCoinbase, 'post_ask') and callable(MockCoinbase.post_ask)
    price = 100.
    order_str = f'Asking {MockCoinbase.State.symbol} at {price}'
    assert order_str == MockCoinbase.post_ask(MockCoinbase.State.symbol, price)

