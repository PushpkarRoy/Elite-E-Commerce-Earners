import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# PostgreSQL connection string
engine = create_engine('postgresql+psycopg2://postgres:Password@localhost:5432/ecommerce_analysis')

# Load CSVs
customers = pd.read_csv("customers.csv")
geolocation = pd.read_csv("geolocation.csv")
order_items = pd.read_csv("order_items.csv")
orders = pd.read_csv("orders.csv")
payments = pd.read_csv("payments.csv")
products = pd.read_csv("products.csv")
sellers = pd.read_csv("sellers.csv")

# Upload dataframes to PostgreSQL
customers.to_sql("customers", engine, index=False, if_exists='replace')
geolocation.to_sql("geolocation", engine, index=False, if_exists='replace')
order_items.to_sql("order_items", engine, index=False, if_exists='replace')
orders.to_sql("orders", engine, index=False, if_exists='replace')
payments.to_sql("payments", engine, index=False, if_exists='replace')
products.to_sql("products", engine, index=False, if_exists='replace')
sellers.to_sql("sellers", engine, index=False, if_exists='replace')

print("✅ All tables uploaded successfully to PostgreSQL!")


