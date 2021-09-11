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
insert_sql = '''INSERT INTO olist_customers (customer_id, customer_unique_id, customer_zip_code_prefix, customer_city, customer_state)
    VALUES (?,?,?,?,?)'''

#"geolocation_zip_code_prefix","geolocation_lat","geolocation_lng","geolocation_city","geolocation_state"


def etl(csv_file, db_file):
    with sqlite3.connect(db_file) as db:
        cur = db.cursor()
        with open('schema.sql') as fp:
            cur.executescript(fp.read())
        cur.executemany(insert_sql, iter_records(csv_file))
        return cur.rowcount



if __name__ == '__main__':
    #insert customers dataset
    count = etl('./dataset/olist_customers_dataset.csv', './db_files/olist_customers_dataset.db')
    print(f'inserted {count} records from olist_customers_dataset.csv')

    #insert geolocation dataset

    #insert order items dataset

    #insert order payments dataset

    #insert order reviews dataset

    #insert orders dataset

    #insert product dataset

    #insert seller dataset

    #insert product category name translation
