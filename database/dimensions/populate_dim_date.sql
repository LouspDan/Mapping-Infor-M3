INSERT INTO dbo.dim_date (date_key, day, month, quarter, year)
SELECT DISTINCT
  invoice_date        AS date_key,
  DAY(invoice_date)   AS day,
  MONTH(invoice_date) AS month,
  DATEPART(QUARTER, invoice_date) AS quarter,
  YEAR(invoice_date)  AS year
FROM staging.stg_account_payables;