IF NOT EXISTS (
  SELECT * FROM sys.tables 
  WHERE name = 'dim_date' AND schema_id = SCHEMA_ID('dbo')
)
CREATE TABLE dbo.dim_date (
  date_key DATE          PRIMARY KEY,
  day      INT           NOT NULL,
  month    INT           NOT NULL,
  quarter  INT           NOT NULL,
  year     INT           NOT NULL
);
