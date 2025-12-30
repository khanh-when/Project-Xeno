import yfinance as yf
import pandas as pd

def extraction(start_date: str, end_date: str, ticker: list[str]) -> pd.DataFrame:
    '''Extract historical stock data(s) from Yahoo Finance in a given date range'''

    def reformat(*dates) -> pd.to_datetime:
        '''parse start/end dates of mixed formats to datetime object'''
        return pd.to_datetime(dates, format='mixed')
    
    return yf.download(ticker, *reformat(start_date, end_date), keepna=True, progress=False)

def extractTicker(ticker: list[str]) -> dict[str: yf.Ticker]:
    return yf.Tickers(ticker).tickers

def main():
    start = '2025/1/1'
    end = '2025/3/1'
    data = extraction(start, end,['AAPL', 'MSFT'])

    print(data.head().to_string())
    print(data.columns)
    print(data.index)
    print(f"Rows: {data.shape[0]} | Columns: {data.shape[1]}")

if __name__ == '__main__':
    main()