import mariadb
from etl_pipeline.extract import extraction
from etl_pipeline.transform import transformation


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
    
    except mariadb.Error as e:
        print(f"Error: MariaDB Server Connection {e}")
        raise mariadb.Error


def main():
    conn = connection('testdb')

if __name__ == '__main__':
    main()




