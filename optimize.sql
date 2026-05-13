-- INDEXES ADD PANNURADHU (Task 5)
CREATE INDEX IF NOT EXISTS idx_fact_user 
ON fact_sales(user_id);

CREATE INDEX IF NOT EXISTS idx_fact_product 
ON fact_sales(product_id);

CREATE INDEX IF NOT EXISTS idx_fact_order 
ON fact_sales(order_id);