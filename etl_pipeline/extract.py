import yfinance as yf
import pandas as pd

tick = 'NVDA'

x = yf.download(tick)

print(x)