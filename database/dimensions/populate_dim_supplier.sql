INSERT INTO dbo.dim_supplier (supplier_id, supplier_name, country)
SELECT DISTINCT
  supplier_id,
  supplier_id        AS supplier_name,  -- à remplacer par nom réel si disponible
  'Unknown'         AS country          -- valeur par défaut ou mappage
FROM staging.stg_account_payables;