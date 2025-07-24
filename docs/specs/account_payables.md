# Spécifications AccountPayables

| Colonne source | Colonne cible   | Type   | Description                               |
|----------------|-----------------|--------|-------------------------------------------|
| invoice_id     | invoice_id      | string | Identifiant unique de la facture          |
| supplier_id    | supplier_id     | string | Identifiant du fournisseur                |
| amount         | amount          | float  | Montant de la facture                     |
| received_date  | invoice_date    | date   | Date de réception de la facture           |
| due_date       | due_date        | date   | Date d’échéance                           |
| load_date      | load_date       | date   | Date d’extraction (ajouté en phase brute) |
