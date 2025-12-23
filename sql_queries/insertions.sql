-- Test Insertion
-- @block
INSERT INTO stock_prices VALUES('MSFT', '2025-1-31', 415.91, 411.87, 416.61, 412.02, 34161900);

-- Delete Test Insertion
-- @block
DELETE FROM stock_prices WHERE (stock_id, trade_date) = ('MSFT', '2025-1-31');