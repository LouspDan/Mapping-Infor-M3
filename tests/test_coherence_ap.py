import os
import pandas as pd
import pytest
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()
engine = create_engine(os.getenv('CONN_STR'))

@pytest.fixture(scope='module')
def df():
    # Lire directement la table staging
    return pd.read_sql('SELECT * FROM staging.stg_account_payables', con=engine)

def test_no_nulls(df):
    # Aucune valeur nulle dans les colonnes clés
    assert df['invoice_id'].notna().all()
    assert df['supplier_id'].notna().all()

def test_amount_positive(df):
    # Les montants doivent être positifs
    assert (df['amount'] > 0).all()

def test_dates_order(df):
    # due_date doit être postérieur ou égal à invoice_date
    assert (df['due_date'] >= df['invoice_date']).all()

def test_not_empty(df):
    assert len(df) > 0, "La table staging.stg_account_payables est vide"
