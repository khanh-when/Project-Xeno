import mariadb
from etl_pipeline.extract import extraction
from etl_pipeline.transform import transformation, formatData
from etl_pipeline.load import loader


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
    start = '3/1/2025'
    end = '5/1/2025'
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

    conn = connection('testdb')

    loader(conn, data)

    conn.commit()    

if __name__ == '__main__':
    main()




