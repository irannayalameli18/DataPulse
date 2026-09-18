import pandas as pd

file_path = "data/raw/Sample - Superstore.xls"

df = pd.read_excel(file_path)

print("===== DATA QUALITY VALIDATION =====")

print("\n1. Missing values:")
print(df.isnull().sum())

print("\n2. Duplicate rows:")
print(df.duplicated().sum())

print("\n3. Unique values:")
print("Order IDs:", df["Order ID"].nunique())
print("Customer IDs:", df["Customer ID"].nunique())
print("Product IDs:", df["Product ID"].nunique())

print("\n4. Quantity validation:")
print("Minimum quantity:", df["Quantity"].min())
print("Maximum quantity:", df["Quantity"].max())
print("Invalid quantity:", (df["Quantity"] <= 0).sum())

print("\n5. Sales validation:")
print("Minimum sales:", df["Sales"].min())
print("Negative sales:", (df["Sales"] < 0).sum())

print("\n6. Discount validation:")
print("Minimum discount:", df["Discount"].min())
print("Maximum discount:", df["Discount"].max())
print("Invalid discount:", ((df["Discount"] < 0) | (df["Discount"] > 1)).sum())

print("\n7. Date validation:")
print("Order date after ship date:",
      (df["Order Date"] > df["Ship Date"]).sum())

print("\n8. Category values:")
print(df["Category"].unique())

print("\n9. Region values:")
print(df["Region"].unique())

print("\n10. Segment values:")
print(df["Segment"].unique())

# for missing 11 postal codes 
print("\n11. Records with missing Postal Code:")
print(df[df["Postal Code"].isna()][
    ["Order ID", "Customer Name", "City", "State", "Postal Code"]
])

# for nan values 
print("\n11. Records with missing Postal Code:")

missing_postal = df[df["Postal Code"].isna()]

print(
    missing_postal[
        [
            "Order ID",
            "Customer Name",
            "City",
            "State",
            "Country/Region",
            "Postal Code"
        ]
    ].to_string(index=False)
)