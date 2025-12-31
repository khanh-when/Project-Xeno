-- Create stocks Table
CREATE TABLE stocks(
    stock_id VARCHAR(10),
    display_name VARCHAR(255),
    industry VARCHAR(100),
    sector VARCHAR(100),
    exchange VARCHAR(100),
    asset_type VARCHAR(50),
    PRIMARY KEY(stock_id)
);

--  Create stock_prices Table 
-- @block
CREATE TABLE stock_prices(
    stock_id VARCHAR(10),
    trade_date DATE,
    open_price DECIMAL(10, 2) UNSIGNED,
    low_price DECIMAL(10, 2) UNSIGNED,
    high_price DECIMAL(10, 2) UNSIGNED,
    close_price DECIMAL(10, 2) UNSIGNED,
    volume BIGINT UNSIGNED,
    PRIMARY KEY(stock_id, trade_date),
    FOREIGN KEY(stock_id) REFERENCES stocks(stock_id)
);

