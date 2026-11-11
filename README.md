# Online Retail Analytics y Segmentación de Clientes

**Análisis de datos transaccionales | Python | SQL | Streamlit | Modelo RFM**

<p align="center">
  <a href="https://online-retail-analytics-5mhtjnsdcsvwh7k5eg2tqt.streamlit.app/">
    <strong>Ver Dashboard Interactivo</strong>
  </a>
</p>

## Descripción del proyecto

Online Retail Analytics es un proyecto de análisis de datos desarrollado en Python que permite procesar información transaccional de un comercio electrónico (e-commerce), analizar el comportamiento de compra y segmentar clientes mediante el modelo **RFM (Recencia, Frecuencia y Valor Monetario)**.

El proyecto integra un proceso de limpieza y transformación de datos, generación de métricas de negocio y visualización interactiva mediante un dashboard desarrollado con Streamlit.

Su objetivo es transformar datos transaccionales en información útil para identificar patrones de compra, evaluar el comportamiento de los clientes y apoyar la toma de decisiones comerciales.

## Objetivos del proyecto

- Limpiar y preparar datos transaccionales para su análisis.
- Identificar y corregir registros nulos o inconsistentes.
- Calcular métricas de Recencia, Frecuencia y Valor Monetario (RFM).
- Identificar segmentos de clientes según su comportamiento de compra.
- Analizar indicadores clave de desempeño (KPIs).
- Visualizar información comercial mediante un dashboard interactivo.
- Aplicar buenas prácticas de organización, modularidad y pruebas de código.

## Tecnologías utilizadas

| Tecnología | Aplicación |
|---|---|
| Python 3.x | Lenguaje principal de desarrollo |
| Pandas | Manipulación, limpieza y transformación de datos |
| Streamlit | Desarrollo del dashboard interactivo |
| Plotly Express | Visualización de datos |
| SQL | Consultas y análisis de información |
| PyTest | Pruebas unitarias |
| Git y GitHub | Control de versiones y documentación |
| Docker | Configuración para contenerización |

## Estructura del proyecto

```text
online-retail-analytics/
│
├── data/
│   └── raw/
│       └── online_retail.csv
│
├── dashboard/
│   └── app.py
│
├── src/
│   ├── transformation.py
│   └── features.py
│
├── sql/
│   └── queries.sql
│
├── tests/
│   └── test_features.py
│
├── .gitignore
├── Dockerfile
├── README.md
└── requirements.txt
```

### Descripción de los directorios y archivos

| Directorio / Archivo | Descripción |
|---|---|
| `data/raw/` | Almacena los datos originales utilizados en el análisis. |
| `dashboard/` | Contiene la aplicación interactiva desarrollada con Streamlit. |
| `src/` | Contiene los módulos de procesamiento y cálculo de métricas. |
| `transformation.py` | Gestiona la limpieza y transformación de los datos. |
| `features.py` | Implementa el cálculo de las métricas RFM. |
| `sql/` | Contiene consultas SQL para el análisis de negocio. |
| `tests/` | Incluye pruebas unitarias para validar el funcionamiento del código. |
| `.gitignore` | Define los archivos y directorios excluidos del control de versiones. |
| `Dockerfile` | Define la configuración para construir un contenedor del proyecto. |
| `requirements.txt` | Lista las dependencias necesarias para ejecutar el proyecto. |

## Descripción funcional

El sistema contempla los siguientes procesos:

1. **Carga de datos:** lectura del conjunto de datos transaccionales.
2. **Limpieza y transformación:** tratamiento de valores nulos, registros inconsistentes y preparación de los datos.
3. **Análisis RFM:** cálculo de las métricas de Recencia, Frecuencia y Valor Monetario para evaluar el comportamiento de los clientes.
4. **Análisis de negocio:** generación de consultas e indicadores relacionados con ingresos, productos y comportamiento comercial.
5. **Visualización:** presentación de los resultados mediante un dashboard interactivo con indicadores y gráficos.

## Modelo RFM

El modelo RFM permite analizar y segmentar clientes a partir de tres dimensiones:

| Métrica | Descripción |
|---|---|
| **Recencia (R)** | Tiempo transcurrido desde la última compra del cliente. |
| **Frecuencia (F)** | Número de compras o transacciones realizadas por el cliente. |
| **Valor Monetario (M)** | Valor económico acumulado de las compras del cliente. |

Estas métricas permiten identificar patrones de comportamiento y generar segmentos útiles para el análisis comercial.

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/EmilioSaulG/online-retail-analytics.git
```

### 2. Acceder al directorio del proyecto

```bash
cd online-retail-analytics
```

### 3. Crear un entorno virtual

```bash
python3 -m venv venv
```

### 4. Activar el entorno virtual

En macOS o Linux:

```bash
source venv/bin/activate
```

En Windows:

```bash
venv\Scripts\activate
```

### 5. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 6. Ejecutar el dashboard

```bash
streamlit run dashboard/app.py
```

Una vez ejecutado el comando, Streamlit proporcionará una dirección local para visualizar la aplicación en el navegador.

## Ejecución de pruebas

Para ejecutar las pruebas unitarias del proyecto, utiliza:

```bash
pytest
```

Esto permitirá verificar el funcionamiento de los módulos y validar los cálculos implementados.

## Arquitectura y calidad del código

El proyecto sigue un enfoque modular para separar las responsabilidades de procesamiento, análisis y visualización.

- **Procesamiento modular:** separación de las operaciones de limpieza y transformación de datos.
- **Ingeniería de características:** cálculo independiente de las métricas RFM.
- **Consultas SQL:** organización de consultas analíticas para obtener indicadores de negocio.
- **Pruebas automatizadas:** utilización de PyTest para validar las funciones implementadas.
- **Visualización interactiva:** integración de los resultados analíticos en una aplicación desarrollada con Streamlit.

## Despliegue

El dashboard se encuentra desplegado mediante **Streamlit Community Cloud**, permitiendo acceder a la aplicación directamente desde un navegador web sin necesidad de instalar dependencias localmente.

**Aplicación en producción:**

[Online Retail Analytics – Dashboard](https://online-retail-analytics-5mhtjnsdcsvwh7k5eg2tqt.streamlit.app/)

La aplicación permite explorar los resultados del análisis de datos, consultar indicadores clave de desempeño (KPIs) y visualizar información relacionada con el comportamiento de compra y la segmentación de clientes mediante el modelo RFM.

## Autor

**Emilio Saúl González**

- GitHub: [@EmilioSaulG](https://github.com/EmilioSaulG)

---

*Proyecto desarrollado con fines de aprendizaje y aplicación práctica de análisis de datos, Python, SQL y visualización de información.*