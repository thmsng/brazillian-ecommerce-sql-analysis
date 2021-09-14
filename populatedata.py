import sqlite3
import pandas as pd


def iter_records(csv_file):
    #read_csv
    df = pd.read_csv(csv_file)

    #turn df into tuples
    for r in df.columns.values:
        df[r] = df[r].map(str)
        df[r] = df[r].map(str.strip)
        tuples = [tuple(x) for x in df.values]

    return tuples


#queries
sql = 'SELECT distance FROM rides WHERE vendor = :vendor'
insert_sql_customer = '''INSERT INTO olist_customers (customer_id, customer_unique_id, customer_zip_code_prefix, customer_city, customer_state) VALUES (?,?,?,?,?)'''
insert_sql_geolocation = '''INSERT INTO olist_geolocation (geolocation_zip_code_prefix, geolocation_lat, geolocation_lng, geolocation_city, geolocation_state) VALUES (?,?,?,?,?)'''
insert_sql_order_items = '''INSERT INTO olist_order_items (order_id, order_item_id, product_id, seller_id, shipping_limit_date, price, freight_value) VALUES (?,?,?,?,?,?,?)'''
insert_sql_order_payments = '''INSERT INTO olist_order_payments (order_id, payment_sequential, payment_type, payment_installments, payment_value) VALUES (?,?,?,?,?)'''
insert_sql_order_reviews = '''INSERT INTO olist_order_reviews (review_id, order_id, review_score, review_comment_title, review_comment_message, review_creation_date, review_answer_timestamp) VALUES (?,?,?,?,?,?,?)'''
insert_sql_orders = '''INSERT INTO olist_orders (order_id, customer_id, order_status, order_purchase_timestamp, order_approved_at, order_delivered_carrier_date, order_delivered_customer_date, order_estimated_delivery_date) VALUES (?,?,?,?,?,?,?,?)'''
insert_sql_products = '''INSERT INTO olist_products (product_id, product_category_name, product_name_lenght, product_description_lenght, product_photos_qty, product_weight_g, product_length_cm, product_height_cm, product_width_cm) VALUES (?,?,?,?,?,?,?,?,?)'''
insert_sql_sellers = '''INSERT INTO olist_sellers (seller_id, seller_zip_code_prefix, seller_city, seller_state) VALUES (?,?,?,?)'''
insert_sql_product_category_name_translation = '''INSERT INTO product_category_name_translation (﻿product_category_name,product_category_name_english) VALUES (?,?)'''


def etl(csv_file, db_file, insert_sql):
    with sqlite3.connect(db_file) as db:
        cur = db.cursor()
        with open('schema.sql') as fp:
            cur.executescript(fp.read())
        cur.executemany(insert_sql, iter_records(csv_file))
    return cur.rowcount



if __name__ == '__main__':
    #insert customers dataset
    #count = etl('./dataset/olist_customers_dataset.csv', './db_files/olist_customers_dataset.db', insert_sql_customer)
    #print(f'inserted {count} records from olist_customers_dataset.csv')

    #insert geolocation dataset
    #count = etl('./dataset/olist_geolocation_dataset.csv', './db_files/olist_geolocation_dataset.db', insert_sql_geolocation)
    #print(f'inserted {count} records from olist_geolocation_dataset.csv')

    #insert order items dataset
    #count = etl('./dataset/olist_order_items_dataset.csv', './db_files/olist_order_items_dataset.db', insert_sql_order_items)
    #print(f'inserted {count} records from olist_order_items_dataset.csv')

    #insert order payments dataset
    #count = etl('./dataset/olist_order_payments_dataset.csv', './db_files/olist_order_payments_dataset.db', insert_sql_order_payments)
    #print(f'inserted {count} records from olist_order_payments_dataset.csv')

    #insert order reviews dataset
    #count = etl('./dataset/olist_order_reviews_dataset.csv', './db_files/olist_order_reviews_dataset.db', insert_sql_order_reviews)
    #print(f'inserted {count} records from olist_order_reviews_dataset.csv')

    #insert orders dataset
    #count = etl('./dataset/olist_orders_dataset.csv', './db_files/olist_orders_dataset.db', insert_sql_orders)
    #print(f'inserted {count} records from olist_orders_dataset.csv')

    #insert product dataset
    #count = etl('./dataset/olist_products_dataset.csv', './db_files/olist_products_dataset.db', insert_sql_products)
    #print(f'inserted {count} records from olist_products_dataset.csv')

    #insert seller dataset
    #count = etl('./dataset/olist_sellers_dataset.csv', './db_files/olist_sellers_dataset.db', insert_sql_sellers)
    #print(f'inserted {count} records from olist_serllers_dataset.csv')

    #insert product category name translation
    #count = etl('./dataset/product_category_name_translation.csv', './db_files/product_category_name_translation.db', insert_sql_product_category_name_translation)
    #print(f'inserted {count} records from product_category_name_translation.csv')




        #insert customers dataset
        count = etl('./dataset/olist_customers_dataset.csv', 'olist.db', insert_sql_customer)
        print(f'inserted {count} records from olist_customers_dataset.csv')

        #insert geolocation dataset
        count = etl('./dataset/olist_geolocation_dataset.csv', 'olist.db', insert_sql_geolocation)
        print(f'inserted {count} records from olist_geolocation_dataset.csv')

        #insert order items dataset
        count = etl('./dataset/olist_order_items_dataset.csv', 'olist.db', insert_sql_order_items)
        print(f'inserted {count} records from olist_order_items_dataset.csv')

        #insert order payments dataset
        count = etl('./dataset/olist_order_payments_dataset.csv', 'olist.db', insert_sql_order_payments)
        print(f'inserted {count} records from olist_order_payments_dataset.csv')

        #insert order reviews dataset
        count = etl('./dataset/olist_order_reviews_dataset.csv', 'olist.db', insert_sql_order_reviews)
        print(f'inserted {count} records from olist_order_reviews_dataset.csv')

        #insert orders dataset
        count = etl('./dataset/olist_orders_dataset.csv', 'olist.db', insert_sql_orders)
        print(f'inserted {count} records from olist_orders_dataset.csv')

        #insert product dataset
        count = etl('./dataset/olist_products_dataset.csv', 'olist.db', insert_sql_products)
        print(f'inserted {count} records from olist_products_dataset.csv')

        #insert seller dataset
        count = etl('./dataset/olist_sellers_dataset.csv', 'olist.db', insert_sql_sellers)
        print(f'inserted {count} records from olist_serllers_dataset.csv')

        #insert product category name translation
        count = etl('./dataset/product_category_name_translation.csv', 'olist.db', insert_sql_product_category_name_translation)
        print(f'inserted {count} records from product_category_name_translation.csv')
