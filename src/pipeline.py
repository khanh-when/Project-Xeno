import mariadb
from etl_pipeline.extract import extraction, extractTicker
from etl_pipeline.transform import formatData, transformation, transformMetaData
from etl_pipeline.load import load_stocks, load_stock_prices, loader

# create database connection
def connection(db_name):
    '''Establish Database Connection to MariaDB Server'''
    try:
        return mariadb.connect(
            user = 'root',
            password = '',
            host = 'localhost',
            port = 3306,
            database = db_name,
            autocommit = False
        )
    
    except mariadb.OperationalError as e:
        print(f"Operational Error: {e}")
        raise mariadb.OperationalError

def main():
    start = '1/1/2025'
    end = '2/1/2025'
    tickers = 'AAPL, MSFT'.split(', ')

    df = extraction(start, end, tickers)
    df2 = formatData(df, tickers)

    for ticker in df2.values():
        print(ticker.head())

    print(list(df2.keys()))

    data = transformation(df, tickers)

    for i in range(40):
        print(data[i])
    
    print(len(data))


    metaData = extractTicker(tickers)

    print(metaData)

    metaData2 = transformMetaData(metaData)

    print(metaData2)

    conn = connection('market_data')
    
    load_stocks(conn, metaData2)

    load_stock_prices(conn, data)

    conn.commit()    

if __name__ == '__main__':
    main()




