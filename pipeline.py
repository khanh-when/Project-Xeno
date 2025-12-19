import mariadb

'''
pipeline.py
 ├─ open DB connection
 ├─ extract
 ├─ transform
 ├─ load(cursor, data)
 ├─ commit
 └─ close connection
 '''

def connection(db_name):
    '''Establish Database Connection to MariaDB Server'''

    try:
        return mariadb.connect(
            user = 'root',
            password = '',
            host = 'localhost',
            port = 3306,
            database = db_name,
            autocommit = True
        )
    
    except mariadb.Error as e:
        print(f"Error: MariaDB Server Connection {e}")
        raise mariadb.Error


if __name__ == '__main__':
    conn = connection('testdb')




