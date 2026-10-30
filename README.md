# Online Retail Analytics y Segmentacion de Clientes

Este proyecto es una solucion analitica desarrollada en Python para procesar datos transaccionales de un e-commerce y segmentar la base de clientes mediante el modelo RFM (Recencia, Frecuencia y Monetario), integrado en un panel interactivo local.

## Estructura del Proyecto

```text
online-retail-analytics/
│
├── data/
│   └── raw/
│       └── online_retail.csv      # Dataset de transacciones
│
├── dashboard/
│   └── app.py                     # Aplicacion web en Streamlit
│
├── src/
│   ├── transformation.py          # Limpieza y preprocesamiento de datos
│   └── features.py                # Calculo de metricas RFM
│
├── README.md                      # Documentacion del proyecto
└── requirements.txt               # Dependencias de Python
