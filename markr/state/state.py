from yaml import safe_load
from os.path import join, dirname, realpath


class State(object):
    CONFIG_FILE_NAME = 'config.yaml'
    CONFIG_PATH = join(dirname(dirname(dirname(realpath(__file__)))), CONFIG_FILE_NAME)

    def __init__(self):
        # Settings
        self.frame_rate = None
        self.exchange = None
        self.symbol = None
        self.refresh_config()
        # Transient states
        self.frame_expiry = None

    def refresh(self):
        # Refresh everything for the next frame including the frame expiration time
        # Run this in a loop that checks current time vs. state frame expiration time
        pass

    def load_config(self):
        with open(self.CONFIG_PATH, 'r') as f:
            config = safe_load(f)
        return config

    def refresh_config(self):
        config = self.load_config()
        self.exchange = config['exchange']
        self.symbol = config['symbol']
        self.frame_rate = config['frame_rate']
        return config

