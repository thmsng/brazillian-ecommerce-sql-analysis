"""Using Pandas to work with databases"""

import pandas as pd

def check_id_length(): #olist_customers_dataset
    #make sure all data have id length of 32 chars -> sql constraint
    df = pd.read_csv('./dataset/olist_customers_dataset.csv')
    print(df.head(5))

    df = df.assign(cus_id_length = (df['customer_id']).apply(len))
    df = df.assign(cus_uid_length = (df['customer_unique_id']).apply(len))

    #df = df.assign(zip_code_length = (df['customer_zip_code_prefix']).apply(str).apply(len))
    print(df.head(20))
    return df.describe()




if __name__ == '__main__':
    print(check_id_length())
