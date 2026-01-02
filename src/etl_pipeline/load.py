import mariadb

def load_stocks(conn, metaData: list) -> None:
    '''load transformed metadata into MariaDB server in batches of 10 rows per execution'''
    query = "INSERT INTO stocks VALUES (?, ?, ?, ?, ?, ?)"

    try:
        with conn.cursor() as cursor:
            for i in range(0, len(metaData), 10):
                cursor.executemany(query, metaData[i: i+10])

        print(f"Successfully inserted stocks: {len(metaData)} Items")
    
    except mariadb.IntegrityError as e:
        print(f"Integrity Error: {e}")
        raise mariadb.IntegrityError

    except mariadb.Error as e:
        print(f"Error: {e}")
        raise mariadb.Error

    return 

def load_stock_prices(conn: mariadb.connect, data: list) -> None:
    '''Tail-recursively loads transformed stock price records into the MariaDB database in fixed-size batches'''

    query = "INSERT INTO stock_prices VALUES (?, ?, ?, ?, ?, ?, ?)"
    
    try:
        with conn.cursor() as cursor:
            for idx in range(0, len(data), 10):
                cursor.executemany(query, data[idx:idx+10])
        
        print(f"Successfully Inserted {len(data)} Items")

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

    except mariadb.Error as e:
        print(f"Error: {e}")
        raise mariadb.Error
    
    return

def loader():
    pass

def main():
    pass

if __name__ == '__main__':
    main()