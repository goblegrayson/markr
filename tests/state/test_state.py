import pytest
import markr


def test_init(MockState):
    assert isinstance(MockState, markr.State)


def test_load_config(MockState):
    config = MockState.load_config()
    assert isinstance(config, dict)
    assert config['frame_rate'] <= 5
    assert config['exchange'].upper() in ['COINBASE']

