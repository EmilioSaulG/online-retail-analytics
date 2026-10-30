import pandas as pd
from datetime import timedelta

def calculate_rfm(df: pd.DataFrame) -> pd.DataFrame:
    #Calculo de métricas RFM ya con datos limpios.
    print("Calculando métricas RFM...")

    reference_date = df['InvoiceDate'].max() + timedelta(days=1)
    #Tomamos la fecha de referencia.

    rfm_df = df.groupby('CustomerID').agg({
        'InvoiceDate': lambda x: (reference_date - x.max()).days,
        'InvoiceNo' : 'nunique',
        'TotalRevenue' : 'sum'
        }).reset_index()
    #Agrupamos R F M

    rfm_df.columns = ['CustomerID','Recency','Frequency','Monetary']
    #Renombramos columnas.

    print("¡Métricas RFM calculadas con éxito!")
    return rfm_df

if __name__ == "__main__":
    from transformation import load_and_clean_data

    file_path = "data/raw/online_retail.csv"
    df_clean = load_and_clean_data(file_path)

    rfm_result = calculate_rfm(df_clean)
    print(rfm_result.head(10))
    print(f'Total de clientes segmentados: {len(rfm_result)}')
#Script para prueba local.