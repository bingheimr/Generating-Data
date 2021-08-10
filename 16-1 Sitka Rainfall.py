import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and precipitation from this file.
    dates, prcps = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        prcp = float(row[3])
        dates.append(current_date)
        prcps.append(prcp)

    # Plot the precipitation.
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, prcps, c='red')

    # Format plot.
    ax.set_title("Daily precipitation - 2018", fontsize=24)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel('Rainfall(in)', fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

print(prcps)
