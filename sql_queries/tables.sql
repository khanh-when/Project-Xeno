-- Create stock Entity Table

--  Create stock_prices Table 
-- @block
CREATE TABLE stock_prices(
    stock_id VARCHAR(6),
    trade_date DATE,
    open_price DECIMAL(10, 2) UNSIGNED,
    low_price DECIMAL(10, 2) UNSIGNED,
    high_price DECIMAL(10, 2) UNSIGNED,
    close_price DECIMAL(10, 2) UNSIGNED,
    volume BIGINT UNSIGNED,
    PRIMARY KEY(stock_id, trade_date)
);

