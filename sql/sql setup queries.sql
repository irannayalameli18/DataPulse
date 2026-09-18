USE master;
GO

IF NOT EXISTS (
    SELECT name
    FROM sys.databases
    WHERE name = N'DataPulseDB'
)
BEGIN
    CREATE DATABASE DataPulseDB;
END
GO

USE DataPulseDB;

SELECT COUNT(*)
FROM sales;

SELECT COUNT(*) AS total_rows
FROM DataPulseDB.dbo.sales;