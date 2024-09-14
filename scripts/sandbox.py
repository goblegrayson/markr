import os
import time
import matplotlib
from coinbase.rest import RESTClient
from matplotlib import pyplot as plt
from time import sleep
import numpy as np

# Load credentials and start up client
coinbase_org = os.environ['CB_ORG']
coinbase_pk = os.environ['CB_PK']
client = RESTClient(api_key=coinbase_org, api_secret=coinbase_pk)

# Configure
hz = 2
chart_time_s = 30
grid_width = 5
symbol = 'BTC-USDC'

# Initial price data
product_data = client.get_product(symbol)
t0 = np.datetime64('now')
p0 = float(product_data['price'])
t1 = t0
p1 = p0

# Chart limits
x_max = t1
x_min = x_max - np.timedelta64(chart_time_s, 's')

# Set up chart
plt.close('all')
plt.ion()
matplotlib.use("TkAgg")
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
fig.suptitle(symbol)

# Make chart pretty
x_labels = [str(x) for x in np.arange(-chart_time_s, 0 + grid_width, grid_width)]
ax.set_xlim([x_min, x_max])
ax.grid(True, 'major', 'both', ls='--', lw=.5, c='k', alpha=.3)
grid_width = np.timedelta64(grid_width, 's')
ax.set_xticks(np.arange(x_min, x_max+grid_width, grid_width).astype(np.datetime64), labels=x_labels)
# ax.set_xticks(np.arange(x_min, x_max+grid_width, grid_width).astype(np.datetime64))
ax.autoscale(enable=True, axis="y", tight=False)

# Start printing prices
i_frame = 0
dt = 1/hz
while True:
    # Update price
    i_frame += 1
    product_data = client.get_product(symbol)
    t0 = t1
    t1 = np.datetime64('now')
    p0 = p1
    p1 = float(product_data['price'])
    # Roll the x-axis
    x_max = t1
    x_min = x_max - np.timedelta64(chart_time_s, 's')
    ax.set_xlim([x_min, x_max])
    ax.set_xticks(np.arange(x_min, x_max + grid_width, grid_width).astype(np.datetime64), labels=x_labels)
    # Plot the tick
    line_color = 'g' if p1 >= p0 else 'r'
    ax.plot([t0, t1], [p0, p1], color=line_color)
    # Redraw plot and wait a frame
    plt.pause(dt)
    if i_frame > chart_time_s / dt:
        ax.lines[0].remove()


