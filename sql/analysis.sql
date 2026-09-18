USE DataPulseDB;

-- 1. Overall Business Metrics
SELECT
    COUNT(*) AS total_records,
    COUNT(DISTINCT order_id) AS total_orders,
    COUNT(DISTINCT customer_id) AS total_customers,
    COUNT(DISTINCT product_id) AS total_products,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    AVG(sales) AS average_sale
FROM sales;


-- 2. Sales by Category
SELECT
    category,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    SUM(quantity) AS total_quantity
FROM sales
GROUP BY category
ORDER BY total_sales DESC;


-- 3. Sales by Region
SELECT
    region,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM sales
GROUP BY region
ORDER BY total_sales DESC;


-- 4. Top 10 Products
SELECT TOP 10
    product_name,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM sales
GROUP BY product_name
ORDER BY total_sales DESC;


-- 5. Top 10 Customers
SELECT TOP 10
    customer_name,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM sales
GROUP BY customer_name
ORDER BY total_sales DESC;

SELECT
    SERVERPROPERTY('ProductVersion') AS ProductVersion,
    SERVERPROPERTY('ProductMajorVersion') AS MajorVersion,
    SERVERPROPERTY('Edition') AS Edition;