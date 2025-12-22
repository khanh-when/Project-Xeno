import pandas as pd
from extract import extraction

def tickerMap(ticker: list[str]) -> dict[str, dict]:
    '''Create a dictionary template for each ticker'''
    return {tick:{} for tick in ticker}

def reorderData(data: pd.DataFrame) -> pd.DataFrame:
    '''Reorder DataFrame columns to Open, Low, High, Close, Volume'''
    return data.loc[:, ['Open', 'Low', 'High', 'Close', 'Volume']]

def restructureData(data: pd.DataFrame, ticker: list[str]) -> dict[str: pd.DataFrame]:
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

def cleanData(data: pd.DataFrame, ticker: list[str]):
    '''clean and format data per ticker'''
    cleanedData = {}
    uncleanedData = restructureData(data, ticker)

    for ticker in uncleanedData.keys():
        uncleanedData[ticker].iloc[[0, 2, 4, 7, 10, 19], 0] = None
        uncleanedData[ticker].iloc[[0, 2, 4, 7, 10, 19], 1] = None
        uncleanedData[ticker].iloc[[0, 2, 4, 7, 10, 19], 3] = None
    
    for ticker in uncleanedData.keys():

        if (uncleanedData[ticker].isna().sum().sum() > 0):
            uncleanedData[ticker].bfill(axis=0, inplace=True)
            uncleanedData[ticker].ffill(axis=0, inplace=True)
    
        cleanedData[ticker] = uncleanedData[ticker].loc[:, ['Open', 'Low', 'High', 'Close']].apply(lambda x: round(x, 2), axis=1).join(uncleanedData[ticker]['Volume'])
        
    
    return cleanedData
    
def transformation(data: pd.DataFrame, ticker: list[str] ):
    '''return final cleaned data as dictionary of DataFrames per ticker'''
    return cleanData(data, ticker)
        
def main():
    
    df = extraction('2025/1/1', '2025/02/1', ['AAPL', 'MSFT'])
    data = transformation(df, ['AAPL', 'MSFT'])

    print(data['MSFT'])
    
if __name__ == '__main__':
    main()