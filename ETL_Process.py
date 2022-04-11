import pandas as pd

# Baca Dataset
print("[1] BACA DATASET")
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/retail_raw_test.csv", low_memory=False)
print("Dataset : \n", df.head())
print("Info    : \n", df.info())

# Ubah Tipe Data
print("\n[2] UBAH TIPE DATA")
df['customer_id'] = df['customer_id'].apply(lambda x: x.split("'")[1]).astype("int64")
df['quantity'] = df['quantity'].apply(lambda x: x.split("'")[1]).astype("int64")
df['item_price'] = df['item_price'].apply(lambda x: x.split("'")[1]).astype("int64")
print("Tpe Data : \n", df.dtypes)

# Melakukan Transform product_value dan mengisi missing value
import math
print("\n[3] Transform product_value menjadi product_id")
def impute_product_value(val):
    if math.isnan(val):
        return "uknown"
    else:
        return 'P' + '{:0>4}'.format(str(val).split('.')[0])
df['product_id'] = df['product_value'].apply(lambda x: impute_product_value(x))
df.drop(['product_value'], axis=1, inplace=True)
print(df.head())

# Melakukan transform order_date 
print("\n[4] Transform order_date menjadi format YYYY-mm_dd")
months_dict = {
    "Jan" : "01",
    "Feb" : "02",
    "Mar" : "03",
    "Apr" : "04",
    "May" : "05",
    "Jun" : "06",
    "Jul" : "07",
    "Aug" : "08",
    "Sep" : "09",
    "Oct" : "10",
    "Nov" : "11",
    "Dec" : "12"
}
df['order_date'] = pd.to_datetime(df['order_date'].apply(lambda x: str(x)[-4:] + "-" + months_dict[str(x)[:3]] + "-" + str(x)[4:7]))
print("Tipe data:\n", df.dtypes)