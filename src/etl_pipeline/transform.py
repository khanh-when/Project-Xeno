import pandas as pd
import datetime
# from extract import extraction

def tickerMap(ticker: list[str]) -> dict[str, dict]:
    '''Create a dictionary template for each ticker'''
    return {tick:{} for tick in ticker}

def reorderData(df: pd.DataFrame) -> pd.DataFrame:
    '''Reorder DataFrame columns to Open, Low, High, Close, Volume'''
    return df.loc[:, ['StockID','Date', 'Open', 'Low', 'High', 'Close', 'Volume']]

def restructureData(df: pd.DataFrame, ticker: list[str]) -> dict[str: pd.DataFrame]:
    '''Restructure extracted DataFrame into dictionary of DataFrames per ticker'''
    tickerData = tickerMap(ticker)

    for tick in tickerData:
        tickerData[tick]['Open'] = df.Open[tick]
        tickerData[tick]['Low'] = df.Low[tick]
        tickerData[tick]['High'] = df.High[tick]
        tickerData[tick]['Close'] = df.Close[tick]
        tickerData[tick]['Volume'] = df.Volume[tick]
    
    return dict(zip(tickerData.keys(), list(map(lambda x: pd.DataFrame(tickerData[x]), tickerData))))

def cleanData(df: pd.DataFrame, ticker: list[str]) -> dict[str: pd.DataFrame]:
    '''Cleaned data through forward/backward fill and rounding into a dictionary of DataFrames per ticker'''
    cleanedData = {}
    uncleanedData = restructureData(df, ticker)

    # Introduce NaN values for testing purposes
    # for ticker in uncleanedData.keys():
    #     uncleanedData[ticker].iloc[[0, 2, 4, 7, 10, 19], 0] = None
    #     uncleanedData[ticker].iloc[[0, 2, 4, 7, 10, 19], 1] = None
    #     uncleanedData[ticker].iloc[[0, 2, 4, 7, 10, 19], 3] = None
    
    for ticker in uncleanedData.keys():
        if (uncleanedData[ticker].isna().sum().sum() > 0):
            uncleanedData[ticker].bfill(axis=0, inplace=True)
            uncleanedData[ticker].ffill(axis=0, inplace=True)
    
        cleanedData[ticker] = uncleanedData[ticker].loc[:, ['Open', 'Low', 'High', 'Close']].apply(lambda x: round(x, 2), axis=1).join(uncleanedData[ticker]['Volume'])
        
    return cleanedData
    
def formatData(df: pd.DataFrame, ticker: list[str]) -> dict[str: pd.DataFrame]:
    '''Format cleaned data into a dictionary of DataFrames per ticker'''
    formattedData = {}
    cleanedData = cleanData(df, ticker)

    for ticker in cleanedData.keys():
        cleanedData[ticker].reset_index(inplace=True)
        tickerID = pd.Series([str(ticker) for i in range(cleanedData[ticker].shape[0])], name='StockID')
        formattedData[ticker] = reorderData(cleanedData[ticker].join(tickerID))

    return formattedData

def transformation(df: pd.DataFrame, ticker: list[str]) -> list[(str, datetime.datetime, float, float, float, float, int)]:
    '''Transform formatted data into a list of tuples in the order of (StockID, Date, Open, Low, High, Close, Volume)'''
    formattedData = formatData(df, ticker)
    unprocessedLst = list(map(lambda x: x.to_numpy(), formattedData.values()))
    processedLst = [tuple(data) for lst in unprocessedLst for data in lst]

    return processedLst

def main():
    # df = extraction('2025/1/1', '2025/2/1', ['AAPL', 'MSFT'])
    
    # data = formatData(df, ['AAPL', 'MSFT'])
    # for ticker in data:
    #     print(data[ticker].head().to_string())

    # transformedData = transformation(df, ['AAPL', 'MSFT'])

    # for i in range(40):
    #     print(transformedData[i])
    pass    


if __name__ == '__main__':
    main()