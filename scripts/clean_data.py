import pandas as pd

# -----------------------------
# 1. Load raw data
# -----------------------------
file_path = "data/raw/Sample - Superstore.xls"

df = pd.read_excel(file_path)

print("Raw rows:", len(df))
print("Raw columns:", len(df.columns))


# -----------------------------
# 2. Clean column names
# -----------------------------
df = df.rename(columns={
    "Row ID": "row_id",
    "Order ID": "order_id",
    "Order Date": "order_date",
    "Ship Date": "ship_date",
    "Ship Mode": "ship_mode",
    "Customer ID": "customer_id",
    "Customer Name": "customer_name",
    "Segment": "segment",
    "Country/Region": "country",
    "City": "city",
    "State": "state",
    "Postal Code": "postal_code",
    "Region": "region",
    "Product ID": "product_id",
    "Category": "category",
    "Sub-Category": "sub_category",
    "Product Name": "product_name",
    "Sales": "sales",
    "Quantity": "quantity",
    "Discount": "discount",
    "Profit": "profit"
})


# -----------------------------
# 3. Convert date columns
# -----------------------------
df["order_date"] = pd.to_datetime(df["order_date"])
df["ship_date"] = pd.to_datetime(df["ship_date"])


# -----------------------------
# 4. Keep missing postal codes
# -----------------------------
# We do NOT invent values for the 11 missing postal codes.
# They remain as missing values.


# -----------------------------
# 5. Create processed folder
# -----------------------------
import os

os.makedirs("data/processed", exist_ok=True)


# -----------------------------
# 6. Export cleaned data
# -----------------------------
output_file = "data/processed/sales_cleaned.csv"

df.to_csv(output_file, index=False)


# -----------------------------
# 7. Final confirmation
# -----------------------------
print("\n===== CLEANING COMPLETE =====")
print("Rows:", len(df))
print("Columns:", len(df.columns))
print("Missing postal codes:", df["postal_code"].isna().sum())
print("Output:", output_file)