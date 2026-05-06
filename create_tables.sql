CREATE TABLE IF NOT EXISTS dim_user (
    user_id VARCHAR(10) PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(150),
    gender VARCHAR(20),
    city VARCHAR(100),
    signup_date DATE
);

CREATE TABLE IF NOT EXISTS dim_product (
    product_id VARCHAR(10) PRIMARY KEY,
    product_name VARCHAR(200),
    category VARCHAR(100),
    brand VARCHAR(100),
    price DECIMAL(10,2),
    rating DECIMAL(3,2)
);

CREATE TABLE IF NOT EXISTS dim_order (
    order_id VARCHAR(10) PRIMARY KEY,
    user_id VARCHAR(10),
    order_date TIMESTAMP,
    order_status VARCHAR(50),
    total_amount DECIMAL(10,2),
    FOREIGN KEY (user_id) REFERENCES dim_user(user_id)
);

CREATE TABLE IF NOT EXISTS dim_date (
    date_id INT PRIMARY KEY,
    full_date DATE,
    day INT,
    month INT,
    quarter INT,
    year INT,
    weekday VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS dim_review (
    review_id VARCHAR(10) PRIMARY KEY,
    order_id VARCHAR(10),
    product_id VARCHAR(10),
    user_id VARCHAR(10),
    rating INT,
    review_text TEXT,
    review_date TIMESTAMP,
    FOREIGN KEY (order_id) REFERENCES dim_order(order_id),
    FOREIGN KEY (product_id) REFERENCES dim_product(product_id),
    FOREIGN KEY (user_id) REFERENCES dim_user(user_id)
);

CREATE TABLE IF NOT EXISTS dim_event (
    event_id VARCHAR(10) PRIMARY KEY,
    user_id VARCHAR(10),
    product_id VARCHAR(10),
    event_type VARCHAR(50),
    event_timestamp TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES dim_user(user_id),
    FOREIGN KEY (product_id) REFERENCES dim_product(product_id)
);

CREATE TABLE IF NOT EXISTS fact_sales (
    order_item_id VARCHAR(10) PRIMARY KEY,
    order_id VARCHAR(10),
    user_id VARCHAR(10),
    product_id VARCHAR(10),
    date_id INT,
    quantity INT,
    item_price DECIMAL(10,2),
    item_total DECIMAL(10,2),
    FOREIGN KEY (order_id) REFERENCES dim_order(order_id),
    FOREIGN KEY (user_id) REFERENCES dim_user(user_id),
    FOREIGN KEY (product_id) REFERENCES dim_product(product_id),
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id)
);