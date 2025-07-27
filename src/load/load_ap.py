import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Chargement des variables d'environnement
load_dotenv()
conn_str = os.getenv('CONN_STR')
if not conn_str:
    raise ValueError("La variable d'environnement CONN_STR n'est pas définie. Vérifiez votre .env.")
engine = create_engine(conn_str)

# Lecture du CSV brut et renommage de colonne
df = pd.read_csv(
    'raw_data/AccountPayables.csv',
    parse_dates=['received_date', 'due_date']
)
df = df.rename(columns={'received_date': 'invoice_date'})

# Ajout de la date de chargement
df['load_date'] = pd.Timestamp.utcnow().date()

# Insertion en staging
try:
    df.to_sql(
        'stg_account_payables',
        schema='staging',
        con=engine,
        if_exists='append',
        index=False
    )
    print('Chargement ELT terminé.')
except Exception as e:
    print(f"Erreur lors du chargement ELT : {e}")
