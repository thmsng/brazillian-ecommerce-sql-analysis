CREATE TABLE IF NOT EXISTS translation (
    id INT auto_increment,
    product_category_name VARCHAR(128),
    product_category_name_english VARCHAR(128)
);

CREATE TABLE IF NOT EXISTS olist_customers (
    customer_id VARCHAR(32),	    -- customer id with mix of numbers and letters (auto generated)
    customer_unique_id VARCHAR(32),	    -- customer id with mix of numbers and letters (auto generated)
    customer_zip_code_prefix INT(5),
    customer_city VARCHAR(128),
    customer_state VARCHAR(2)
);

CREATE TABLE IF NOT EXISTS olist_geolocation (
    geolocation_zip_code_prefix VARCHAR(5),
    geolocation_lat DECIMAL(17,15),
    geolocation_lng DECIMAL(18,15),
    geolocation_city VARCHAR(128),
    geolocation_state VARCHAR(2)
);

CREATE TABLE IF NOT EXISTS olist_order_items (
    order_id VARCHAR(32),
    order_item_id INT,
    product_id VARCHAR(32),
    seller_id VARCHAR(32),
    shipping_limit_date DATE,
    price DECIMAL,
    freight_value DECIMAL
);

CREATE TABLE IF NOT EXISTS olist_order_payments (
    order_id VARCHAR(32),
    payment_sequential INT(3),
    payment_type VARCHAR,
    payment_installments INT,
    payment_value DECIMAL
);

CREATE TABLE IF NOT EXISTS olist_order_reviews (
    review_id VARCHAR(32),
    order_id VARCHAR(32),
    review_score INT(1),
    review_comment_title VARCHAR(128),
    review_comment_message TEXT,
    review_creation_date DATE,
    review_answer_timestamp DATE
);

CREATE TABLE IF NOT EXISTS olist_orders (
    order_id VARCHAR(32),
    customer_id VARCHAR(32),
    order_status VARCHAR(128),
    order_purchase_timestamp DATE,
    order_approved_at DATE,
    order_delivered_carrier_date DATE,
    order_delivered_customer_date DATE,
    order_estimated_delivery_date DATE
);

CREATE TABLE IF NOT EXISTS olist_products (
    product_id VARCHAR(32),
    product_category_name VARCHAR(128),
    product_name_lenght INT,
    product_description_lenght INT,
    product_photos_qty INT,
    product_weight_g INT,
    product_length_cm INT,
    product_height_cm INT,
    product_width_cm INT
);

CREATE TABLE IF NOT EXISTS olist_sellers (
    seller_id VARCHAR(32),
    seller_zip_code_prefix INT,
    seller_city VARCHAR(128),
    seller_state VARCHAR(2)
);
