import pytest
import markr


def test_init(MockExchange):
    assert isinstance(MockExchange, markr.exchanges.ExchangeBase)
    assert isinstance(MockExchange, markr.exchanges.Coinbase)

