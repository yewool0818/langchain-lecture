# filename: plot_stocks.py
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define the start date of the year and today's date
start_date = '2024-01-01'
end_date = '2024-06-21'

# Fetch historical data for NVDA and TSLA
tickers = ["NVDA", "TSLA"]
data = yf.download(tickers, start=start_date, end=end_date, progress=False)['Adj Close']

# Ensure the data frame is not empty
if data.empty:
    raise ValueError("No data fetched. Check network connectivity or ticker symbols.")

# Calculate the relative gain from the start of the year in percent
relative_gains = ((data - data.iloc[0]) / data.iloc[0]) * 100

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(relative_gains.index, relative_gains['NVDA'], label='NVDA YTD Gain')
plt.plot(relative_gains.index, relative_gains['TSLA'], label='TSLA YTD Gain')
plt.title('YTD Stock Gains 2024: NVDA vs TSLA')
plt.xlabel('Date')
plt.ylabel('Percentage Gain (%)')
plt.legend()
plt.grid(True)

# Save the plot to a file
plt.savefig('ytd_stock_gains.png')
plt.show()