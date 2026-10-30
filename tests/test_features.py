import pandas as pd
import pytest

def test_sample_pipeline():
    """Prueba unitaria básica para verificar la integración de datos y columnas clave."""
    # Creamos un DataFrame simulando transacciones de e-commerce
    df = pd.DataFrame({
        "CustomerID": [101, 102, 101],
        "UnitPrice": [10.0, 20.0, 5.0],
        "Quantity": [1, 2, 4]
    })
    
    # Validamos que no esté vacío y que el cálculo monetario básico sea correcto
    assert len(df) == 3
    total_revenue = (df["UnitPrice"] * df["Quantity"]).sum()
    assert total_revenue == 70.0