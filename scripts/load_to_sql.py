import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# SQL Server details
server = r"LAPTOP-VL54MEAQ\SQLEXPRESS"
database = "DataPulseDB"

# Connection string
connection_string = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    f"SERVER={server};"
    f"DATABASE={database};"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

# Create SQLAlchemy engine
engine = create_engine(
    "mssql+pyodbc:///?odbc_connect=" + quote_plus(connection_string)
)

# Read cleaned CSV
file_path = "data/processed/sales_cleaned.csv"
df = pd.read_csv(file_path)

print("CSV rows:", len(df))

# Load into SQL Server
df.to_sql(
    "sales",
    con=engine,
    if_exists="replace",
    index=False
)

print("Data loaded successfully into DataPulseDB!")
print("Table created: sales")
print("Rows loaded:", len(df))