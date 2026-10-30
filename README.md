# Online Retail Analytics y Segmentacion de Clientes

Este proyecto es una solucion analitica desarrollada en Python para procesar datos transaccionales de un e-commerce y segmentar la base de clientes mediante el modelo RFM (Recencia, Frecuencia y Monetario), integrado en un panel interactivo local.

## Estructura del Proyecto

```
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
```
Descripcion General
El sistema automatiza la limpieza de registros nulos o inconsistentes, calcula las metricas de comportamiento de compra para cada cliente y despliega un panel de control interactivo. Permite consultar los indicadores clave de desempeño (KPIs), analizar visualmente a los clientes con mayor volumen de gasto y explorar la informacion de forma dinamica mediante filtros de negocio.

##Requisitos y Tecnologias
°Python 3.x

°Pandas (Manipulacion de datos)

°Streamlit (Desarrollo del dashboard)

°Plotly Express (Visualizacion interactiva)

## Instrucciones de Instalacion y Ejecucion

1. Asegurate de estar ubicado en la carpeta raiz del proyecto en tu terminal.
2. Instala las librerias requeridas ejecutando:
   ```bash
   pip install pandas streamlit plotly

   
# Online Retail Analytics Platform

## Descripción General
El sistema automatiza la limpieza de registros nulos o inconsistentes, calcula las métricas de comportamiento de compra para cada cliente y despliega un panel de control interactivo. Permite consultar los indicadores clave de desempeño (KPIs), analizar visualmente a los clientes con mayor volumen de gasto y explorar la información de forma dinámica mediante filtros de negocio.

---

## Requisitos y Tecnologías
* **Python 3.x**
* **Pandas**: Manipulación y limpieza de datos
* **Streamlit**: Desarrollo del dashboard web interactivo
* **Plotly Express**: Visualización interactiva de datos
* **PyTest**: Pruebas unitarias automatizadas

---

## Instrucciones de Instalación y Ejecución

1. Asegúrate de estar ubicado en la carpeta raíz del proyecto en tu terminal.
2. Instala las librerías requeridas ejecutando:
   ```bash
   pip install -r requirements.txtn Streamlit Community Cloud para su consumo en la nube en tiempo real.
