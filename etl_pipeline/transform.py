import pandas as pd
from extract import extraction

def tickerMap(ticker: list[str]) -> dict[str, dict]:
    '''Create a dictionary template for each ticker'''
    return {tick:{} for tick in ticker}

def reorderData(data: pd.DataFrame) -> pd.DataFrame:
    '''Reorder DataFrame columns to Open, Low, High, Close, Volume'''
    return data.loc[:, ['Open', 'Low', 'High', 'Close', 'Volume']]

def restructureData(data: pd.DataFrame, ticker) -> dict[str, pd.DataFrame]:
    '''Restructure extracted DataFrame into dictionary of DataFrames per ticker'''
    tickerData = tickerMap(ticker)
    df = reorderData(data)

    for tick in tickerData:
        tickerData[tick]['Open'] = df.Open[tick]
        tickerData[tick]['Low'] = df.Low[tick]
        tickerData[tick]['High'] = df.High[tick]
        tickerData[tick]['Close'] = df.Close[tick]
        tickerData[tick]['Volume'] = df.Volume[tick]
    
    return dict(zip(tickerData.keys(), list(map(lambda x: pd.DataFrame(tickerData[x]), tickerData))))

def main():
    
    df = extraction('2025/1/1', '2025/3/1', ['AAPL', 'MSFT'])
    data = restructureData(df, ['AAPL', 'MSFT'])

if __name__ == '__main__':
    main()