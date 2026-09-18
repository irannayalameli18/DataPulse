# DataPulse — Sales Data Pipeline & Analytics

DataPulse is a sales data pipeline and analytics project built using Python, Pandas, SQL Server, and Power BI.

The project takes raw sales data, validates and cleans it using Python, stores the processed data in SQL Server for analysis, and uses Power BI to visualize key business metrics and trends.

## Project Workflow

```
Raw Sales Data
      ↓
Python + Pandas
      ↓
Data Validation & Cleaning
      ↓
Processed CSV
      ↓
SQL Server
      ↓
T-SQL Analysis

Processed CSV
      ↓
Power BI
      ↓
Interactive Dashboard


Technologies Used
Python
Pandas
SQL Server
T-SQL
SQLAlchemy
PyODBC
Power BI
Git & GitHub
Key Features
Data Inspection
Inspected the raw Superstore dataset.
Examined data types, record counts, and column structure.
Data Validation
Checked missing values.
Checked duplicate records.
Validated sales and quantity values.
Checked discount ranges.
Validated order and shipping dates.
Reviewed categorical values.
Data Cleaning
Standardized column names.
Converted date fields into appropriate formats.
Preserved missing postal-code values when reliable replacement data was unavailable.
Generated a cleaned CSV dataset for downstream analysis.
SQL Analysis

The processed dataset was loaded into SQL Server and analyzed using T-SQL queries for:

Sales performance
Profit analysis
Regional performance
Category and sub-category analysis
Customer and product insights
Monthly trends
Power BI Dashboard

The project includes an interactive Power BI dashboard containing:

Total Orders
Total Customers
Total Sales
Total Profit
Monthly Sales Trend
Profit by Region
Sales by Category
Sales by Region
Top 10 Products by Sales
Category and Region filters
Dataset

The project uses the Sample Superstore dataset containing:

9,994 sales records
5,009 unique orders
793 unique customers
1,862 unique products

The raw dataset is stored in:

data/raw/Sample - Superstore.xls

The processed dataset is stored in:

data/processed/sales_cleaned.csv

Project Structure

DataPulse/
│
├── data/
│   ├── raw/
│   │   └── Sample - Superstore.xls
│   └── processed/
│       └── sales_cleaned.csv
│
├── scripts/
│   ├── inspect_data.py
│   ├── validate_data.py
│   ├── clean_data.py
│   └── load_to_sql.py
│
├── sql/
│   ├── analysis.sql
│   └── sql setup queries.sql
│
├── Sales Dashboard.pbix
├── project report.txt
├── .gitignore
└── README.md

How to Run
1. Install Dependencies
pip install pandas sqlalchemy pyodbc
2. Inspect the Dataset
python .\scripts\inspect_data.py
3. Validate the Data
python .\scripts\validate_data.py
4. Clean and Process the Data
python .\scripts\clean_data.py

This generates:

data/processed/sales_cleaned.csv

5. Load Data into SQL Server
python .\scripts\load_to_sql.py

The processed data is loaded into the DataPulseDB SQL Server database.

6. Run SQL Analysis

Open the SQL files in SQL Server Management Studio (SSMS) and execute the analysis queries.

7. View the Dashboard

Open:

Sales Dashboard.pbix

The Power BI dashboard uses the processed CSV output for visualization.

Key Results
9,994 sales records
5,009 unique orders
793 unique customers
1,862 unique products
Approximately $2.30M in total sales
Approximately $286.40K in total profit
Project Outcome

DataPulse demonstrates an end-to-end data workflow:

Data Ingestion → Validation → Cleaning → Transformation → SQL Analysis → Visualization

The project strengthened practical skills in Python-based data processing, SQL, data analysis, and business intelligence.

Author

Iranna Yalameli

B.Tech — Electronics and Computer Engineering
