import pandas as pd

def check_id_length(): #olist_customers_dataset
    #make sure all data have id length of 32 chars -> sql constraint
    df = pd.read_csv('./dataset/olist_customers_dataset.csv')
    print(df.head(5))

    df = df.assign(cus_id_length = (df['customer_id']).apply(len))
    df = df.assign(cus_uid_length = (df['customer_unique_id']).apply(len))

    #df = df.assign(zip_code_length = (df['customer_zip_code_prefix']).apply(str).apply(len))
    print('head(20):')
    print(df.head(20))
    print()
    print()
    return df

def check_length(csv_file):
    df = pd.read_csv(csv_file)
    print('head(5):')
    print(df.head(5))
    print()
    print()

    #check len of each column
    print('head(5): each column s length')
    for i in df.columns:
        df[i+'_len'] = df[i].apply(str).apply(len)
        print(df[i].head(5))
        print(df[i+'_len'].head(5))
        print('-----')

    print()
    return df

if __name__ == '__main__':
    #print(check_id_length().describe())
    #print(check_length('./dataset/olist_geolocation_dataset.csv').describe())
    #print(check_length('./dataset/olist_order_items_dataset.csv').describe())
    #print(check_length('./dataset/olist_order_payments_dataset.csv').describe())
    #print(check_length('./dataset/olist_order_reviews_dataset.csv').describe())
    #print(check_length('./dataset/olist_orders_dataset.csv').describe())
    #print(check_length('./dataset/olist_products_dataset.csv').describe())
    #print(check_length('./dataset/olist_sellers_dataset.csv').describe())
    print(check_length('./dataset/product_category_name_translation.csv').describe())
