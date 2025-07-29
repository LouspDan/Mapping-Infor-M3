IF NOT EXISTS (
  SELECT * FROM sys.tables 
  WHERE name = 'dim_supplier' AND schema_id = SCHEMA_ID('dbo')
)
CREATE TABLE dbo.dim_supplier (
  supplier_id   NVARCHAR(50) PRIMARY KEY,
  supplier_name NVARCHAR(255),
  country       NVARCHAR(100)
);
