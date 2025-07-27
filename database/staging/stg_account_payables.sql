IF NOT EXISTS (SELECT * FROM sys.schemas WHERE name = 'staging')
  EXEC('CREATE SCHEMA staging');
CREATE TABLE staging.stg_account_payables (
    invoice_id NVARCHAR(50) NOT NULL,
    supplier_id NVARCHAR(50) NOT NULL,
    amount FLOAT NOT NULL,
    invoice_date DATE NOT NULL,
    due_date DATE NOT NULL,
    load_date DATE NOT NULL
);