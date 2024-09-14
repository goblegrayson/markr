import pytest
import markr


@pytest.fixture
def MockState():
    return markr.State()


@pytest.fixture
def MockExchange(MockState):
    return markr.Coinbase(MockState)


@pytest.fixture
def MockCoinbase(MockState):
    return markr.Coinbase(MockState)







