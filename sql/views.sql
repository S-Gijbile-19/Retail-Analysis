-- View 1: Sales Summary
CREATE VIEW IF NOT EXISTS vw_sales_summary AS
SELECT 
    u.city,
    p.category,
    p.brand,
    SUM(f.item_total) AS total_revenue,
    COUNT(f.order_item_id) AS total_orders,
    AVG(r.rating) AS avg_rating
FROM fact_sales f
JOIN dim_user u ON f.user_id = u.user_id
JOIN dim_product p ON f.product_id = p.product_id
LEFT JOIN dim_review r ON f.product_id = r.product_id
GROUP BY u.city, p.category, p.brand;

-- View 2: Monthly Revenue
CREATE VIEW IF NOT EXISTS vw_monthly_revenue AS
SELECT 
    d.year,
    d.month,
    SUM(f.item_total) AS monthly_revenue,
    COUNT(f.order_item_id) AS total_orders
FROM fact_sales f
JOIN dim_date d ON f.date_id = d.date_id
GROUP BY d.year, d.month;

-- View 3: Product Performance
CREATE VIEW IF NOT EXISTS vw_product_performance AS
SELECT 
    p.product_name,
    p.category,
    p.brand,
    SUM(f.item_total) AS total_revenue,
    AVG(r.rating) AS avg_rating,
    COUNT(f.order_item_id) AS total_sold
FROM fact_sales f
JOIN dim_product p ON f.product_id = p.product_id
LEFT JOIN dim_review r ON f.product_id = r.product_id
GROUP BY p.product_name, p.category, p.brand;