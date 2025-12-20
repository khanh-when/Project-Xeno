import pandas as pd
from extract import extraction



def main():
    data = extraction('2025/1/1', '2025/3/1', 'AAPL')
    print(data.head())

if __name__ == '__main__':
    main()