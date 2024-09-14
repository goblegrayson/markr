from .ExchangeBase import ExchangeBase
from os import environ
from coinbase.rest import RESTClient


class Coinbase(ExchangeBase):
    def __init__(self, State, testing=True):
        super().__init__(state=State, testing=testing)
        coinbase_org = environ['CB_ORG']
        coinbase_pk = environ['CB_PK']
        if not coinbase_org or not coinbase_pk:
            raise ValueError('Coinbase API info not set. Ensure CB_ORG and CB_PK are set in your environment variables.')
        self.client = RESTClient(api_key=coinbase_org, api_secret=coinbase_pk)

    def get_price(self, symbol):
        product_data = self.client.get_product(product_id=symbol)
        return product_data

    def post_bid(self, symbol, price):
        order_str = f'Bidding {symbol} at {price}'
        if not self.testing:
            print(order_str)
        return order_str

    def post_ask(self, symbol, price):
        order_str = f'Asking {symbol} at {price}'
        if not self.testing:
            print(order_str)
        return order_str

