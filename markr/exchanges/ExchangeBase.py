from abc import ABC, abstractmethod


class ExchangeBase(ABC):
    def __init__(self, state, testing=True):
        self.State = state
        self.testing = testing

    @abstractmethod
    def post_bid(self, symbol, price):
        pass

    @abstractmethod
    def post_ask(self, symbol, price):
        pass

    @abstractmethod
    def get_price(self, symbol):
        pass

    def post_marks(self, symbol, bid_price, ask_price):
        self.post_bid(symbol, bid_price)
        self.post_ask(symbol, ask_price)

