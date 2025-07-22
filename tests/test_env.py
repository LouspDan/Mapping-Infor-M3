import sys
import sqlalchemy
import pyodbc

def test_python_version():
    # Vérifier Python ≥ 3.9
    v = sys.version_info
    assert v.major == 3 and v.minor >= 9

def test_sqlalchemy_import():
    assert hasattr(sqlalchemy, "__version__")

def test_pyodbc_import():
    assert hasattr(pyodbc, "version") or hasattr(pyodbc, "__version__")
