import pandas as pd
import numpy as np

def load_and_clean_data(filepath: str) -> pd.DataFrame:
    
    #Carga el dataset de Online Retail, limpia valores nulos y procesa los tipos de datos.
    
    print("Cargando datos...")
    df = pd.read_csv(filepath)    

    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    #Conversión para análisis temporales

    initial_shape = df.shape
    df = df.dropna(subset=['CustomerID','Description'])
    print(f"Se eliminaron{initial_shape[0] - df.shape[0]} filas con valores nulos en CostumerID o Description.")
    #Eliminamos valores nulos en CostumerID y Description
    #Guardamos copia para posible RFM

    df['TotalRevenue'] = df['Quantity'] * df['UnitPrice']
    #Columna con el ingreso total

    df['IsCancelled'] = df['InvoiceNo'].astype(str).str.startswith('C') | (df['Quantity'] < 0)
    #Identificar cancelaciones
    #Creamos un identificador para las cancelaciones

    print("Datos limpios y listos para el análisis.")
    return df

if __name__ == "__main__":
    file_path = "data/raw/online_retail.csv"
    df_clean = load_and_clean_data(file_path)
    print(df_clean.info())
    print(f'Total de registros limpios: {len(df_clean)}')
#Script para pruebla local.