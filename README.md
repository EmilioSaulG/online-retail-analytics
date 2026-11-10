# Online Retail Analytics y Segmentación de Clientes

Este proyecto es una solución analítica desarrollada en Python para procesar datos transaccionales de un e-commerce y segmentar la base de clientes mediante el modelo RFM (Recencia, Frecuencia y Monetario), integrado en un panel interactivo.

---

## Estructura del Proyecto

online-retail-analytics/
├── data/
│   └── raw/
│       └── online_retail.csv    # Dataset de transacciones
├── dashboard/
│   └── app.py                  # Aplicación web en Streamlit
├── src/
│   ├── transformation.py       # Limpieza y preprocesamiento de datos
│   └── features.py             # Cálculo de métricas RFM
├── sql/
│   └── queries.sql             # Consultas analíticas en SQL
├── tests/
│   └── test_features.py        # Pruebas unitarias con PyTest
├── .gitignore                  # Exclusiones de Git
├── Dockerfile                  # Configuración de contenedor
├── README.md                   # Documentación del proyecto
└── requirements.txt            # Dependencias de Python

---

## Descripción General

El sistema automatiza la limpieza de registros nulos o inconsistentes, calcula las métricas de comportamiento de compra para cada cliente y despliega un panel de control interactivo. Permite consultar los indicadores clave de desempeño (KPIs), analizar visualmente a los clientes con mayor volumen de gasto y explorar la información de forma dinámica mediante filtros de negocio.

---

## Requisitos y Tecnologías

* Python 3.x
* Pandas: Manipulación y limpieza de datos
* Streamlit: Desarrollo del dashboard web interactivo
* Plotly Express: Visualización interactiva de datos
* PyTest: Pruebas unitarias automatizadas

---

## Instrucciones de Instalación y Ejecución

1. Asegúrate de estar ubicado en la carpeta raíz del proyecto en tu terminal.
2. Instala las librerías requeridas ejecutando:
   pip install -r requirements.txt
3. Ejecuta la aplicación web con el siguiente comando:
   streamlit run dashboard/app.py

---

## Arquitectura y Calidad de Código

El proyecto está diseñado bajo principios de modularidad e ingeniería de software:

* Procesamiento Modular (src/): Separación limpia entre la ingesta de datos, la limpieza de registros y el cálculo del modelo RFM.
* Capa de Consultas SQL (sql/): Consultas analíticas estructuradas para la extracción de métricas clave de negocio, productos Top e ingresos mensuales.
* Pruebas Automatizadas (tests/): Pruebas unitarias integradas con pytest para garantizar la integridad de las transformaciones y cálculos numéricos.
* Despliegue Continuo: Integración directa con Streamlit Community Cloud para su consumo en la nube en tiempo real.