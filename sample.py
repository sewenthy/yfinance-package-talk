import yfinance as yf
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

"""
Single stock access--through the Ticker module
"""
msft = yf.Ticker("MSFT")
msft.info
"""
returns a dictionary of basic information such as
sector, employees, business summary, industry, etc.
"""

hist = msft.history(period="max")
"""
output a pandas dataframe with a timeseries information
on open, close, high, low, volume, dividends, and stock splits.
"""

plt.plot(hist[["Open","Close"]])
plt.title("MSFT")
plt.xlabel("Year")
plt.legend(["Open","Close"])
plt.show()

"""
Raw Data Downloads
programmatically, pull many symbols for securities with
custom ranges
"""
data = yf.download("AAPL GME", start="2021-01-01", end="2022-01-01")

plt.plot(data["High"][['AAPL', 'GME']])
plt.title("AAPL and GME Highs in 2021")
plt.xlabel("Time")
plt.legend(["AAPL","GME"])
plt.show()
