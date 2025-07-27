import pandas as pd
import pytest

RAW = 'raw_data/AccountPayables.csv'
SPECS = {
    'invoice_id': 'invoice_id',
    'supplier_id': 'supplier_id',
    'amount': 'amount',
    'received_date': 'invoice_date',
    'due_date': 'due_date'
}

def test_mapping_columns_present():
    df = pd.read_csv(RAW)
    for src in SPECS.keys():
        assert src in df.columns, f"Colonne source manquante : {src}"

def test_mapping_target_unique():
    targets = list(SPECS.values())
    assert len(targets) == len(set(targets)), "Conflit dans les noms de colonnes cibles"

def test_amount_dtype():
    df = pd.read_csv(RAW)
    assert pd.api.types.is_float_dtype(df['amount']), "La colonne amount n'est pas de type float"

