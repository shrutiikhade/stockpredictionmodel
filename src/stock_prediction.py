import yfinance as yf
import pandas as pd

# Download data for HDFC from Yahoo Finance
ticker = 'HDFCBANK.NS'  # HDFC Bank's ticker symbol on NSE
data = yf.download(ticker, start='2020-01-01', end='2023-12-31')

# Save data to CSV
data.to_csv('../data/hdfc_stock_data.csv')