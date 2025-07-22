import os
from dotenv import load_dotenv
import sqlalchemy
from sqlalchemy import text

# Charger les variables d'environnement depuis .env
load_dotenv()

SERVER   = os.getenv("SA_HOST")
PORT     = os.getenv("SA_PORT")
DATABASE = os.getenv("SA_DB")
USERNAME = os.getenv("SA_USER")
PASSWORD = os.getenv("SA_PASSWORD")

connection_string = (
    f"mssql+pyodbc://{USERNAME}:{PASSWORD}"
    f"@{SERVER}:{PORT}/{DATABASE}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
)

def test_sql_connection():
    engine = sqlalchemy.create_engine(connection_string, echo=False)
    with engine.connect() as conn:
        result = conn.execute(text("SELECT @@VERSION;"))
        version = result.scalar()
        assert "Microsoft SQL Server" in version
        print("Connexion OK – version :", version)

