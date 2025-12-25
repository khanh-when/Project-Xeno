import pandas as pd
import mariadb

def loader(conn: mariadb.connect, data: list):
    '''load transformed data into MariaDB server in batches of 10 rows per execution'''
    query = "INSERT INTO stock_prices VALUES (?, ?, ?, ?, ?, ?, ?)"

    try:
        with conn.cursor() as cursor:
            for i in range(0, len(data), 10):
                cursor.executemany(query, data[i:i+10])
        
        print(f"Successfully Inserted {len(data)} Values")
    
    except mariadb.IntegrityError as e:
        print(f"Integrity Error: {e}")
        raise mariadb.IntegrityError

    except mariadb.Error as e:
        print(f"Error: {e}")
        raise mariadb.Error

def main():
    pass

if __name__ == '__main__':
    main()