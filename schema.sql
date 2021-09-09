CREATE TABLE IF NOT EXISTS olist_customers (
    customer_id VARCHAR(32),	    -- customer id with mix of numbers and letters (auto generated)
    customer_unique_id VARCHAR(32),	    -- customer id with mix of numbers and letters (auto generated)
    customer_zip_code_prefix INT(5),
    customer_city VARCHAR(128),
    customer_state VARCHAR(2)
);
