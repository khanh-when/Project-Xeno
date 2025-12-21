import pandas as pd
from extract import extraction

def reorder(data: pd.DataFrame) -> pd.DataFrame:
    '''Reorder DataFrame columns to Open, Low, High, Close, Volume'''
    return data.loc[:, ['Open', 'Low', 'High', 'Close', 'Volume']]

def main():
    data = reorder(extraction('2025/1/1', '2025/3/1', ['AAPL', 'MSFT']))


if __name__ == '__main__':
    main()