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


def check_geo_length():
    df = pd.read_csv('./dataset/olist_geolocation_dataset.csv')
    print(df.head(5))

    for i in df.columns:
        df = df.assign(l1 = (df[i].apply(len)))

    print(df.head(10))
    return df.describe()

if __name__ == '__main__':
    print(check_id_length())


#"geolocation_zip_code_prefix","geolocation_lat","geolocation_lng","geolocation_city","geolocation_state"
