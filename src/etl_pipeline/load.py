import mariadb

def load_stocks(conn, metaData: list) -> None:
    '''Tail-recursively loads transformed stock metadata into the MariaDB database in fixed-size batches'''
    
    # prepared insert query
    query = "INSERT INTO stocks VALUES (?, ?, ?, ?, ?, ?)"

    # try to insert metadata in batches
    try:
        with conn.cursor() as cursor:
            for idx in range(0, len(metaData), 10):
                cursor.executemany(query, metaData[idx: idx+10])

        print(f"Successfully inserted {len(metaData)} stock metadata records")
    
    # on integrity error, split the metadata and retry
    except mariadb.IntegrityError as e:
        print(f"Integrity Error: {e}")

        # base case: if metadata length is 1 or less, return
        if len(metaData) <= 1:
            return
        
        split = len(metaData) // 2

        # recursively call load_stocks on first half
        load_stocks(conn, metaData[idx:split])

        # recursively call load_stocks on second half
        load_stocks(conn, metaData[split:])

    # except other mariadb errors
    except mariadb.Error as e:
        print(f"Error: {e}")
        raise mariadb.Error

    return 

def load_stock_prices(conn: mariadb.connect, data: list) -> None:
    '''Tail-recursively loads transformed stock price records into the MariaDB database in fixed-size batches'''

    # prepared insert query
    query = "INSERT INTO stock_prices VALUES (?, ?, ?, ?, ?, ?, ?)"
    
    # try to insert data in batches
    try:
        with conn.cursor() as cursor:
            for idx in range(0, len(data), 10):
                cursor.executemany(query, data[idx:idx+10])
        
        print(f"Successfully Inserted {len(data)} Stock Price Records")

    #  on integrity error, split the data and retry
    except mariadb.IntegrityError as e:
        print(f"Integrity Error: {e}")

    # base case: if data length is 1 or less, return
        if len(data) <= 1:
            return

        split = len(data) // 2

        # recursively call load_stock_prices on first half
        load_stock_prices(conn, data[idx:split])

        # recursively call load_stock_prices on second half
        load_stock_prices(conn, data[split:])

    # except other mariadb errors
    except mariadb.Error as e:
        print(f"Error: {e}")
        raise mariadb.Error
    
    return

def loader(conn: mariadb.connect, metaData: list, data: list) -> None:
    '''Orchestrates the loading of stock metadata and stock price records into the MariaDB database'''
    
    # Due to primary key constraints, load stock metadata first
    load_stocks(conn, metaData)

    # next, load stock price records
    load_stock_prices(conn, data)

    return

def main():
    pass

if __name__ == '__main__':
    main()