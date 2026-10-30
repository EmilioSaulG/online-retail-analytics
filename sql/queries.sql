-- PROYECTO: Online Retail Analytics
-- DESCRIPCIÓN: Consultas SQL para análisis de transacciones y segmentación RFM

-- 1. Limpieza inicial: Identificar transacciones válidas (excluyendo devoluciones y nulos)
SELECT 
    InvoiceNo,
    StockCode,
    Description,
    Quantity,
    InvoiceDate,
    UnitPrice,
    CustomerID,
    Country
FROM online_retail
WHERE CustomerID IS NOT NULL 
  AND Quantity > 0 
  AND UnitPrice > 0;

-- 2. Análisis de Ingresos Totales por Mes (Tendencia de Ventas)
SELECT 
    DATE_FORMAT(InvoiceDate, '%Y-%m') AS YearMonth,
    SUM(Quantity * UnitPrice) AS TotalRevenue,
    COUNT(DISTINCT InvoiceNo) AS TotalTransactions,
    COUNT(DISTINCT CustomerID) AS ActiveCustomers
FROM online_retail
WHERE CustomerID IS NOT NULL AND Quantity > 0
GROUP BY YearMonth
ORDER BY YearMonth ASC;

-- 3. Top 10 Productos con Mayor Generación de Ingresos
SELECT 
    StockCode,
    Description,
    SUM(Quantity) AS TotalUnitsSold,
    SUM(Quantity * UnitPrice) AS TotalRevenue
FROM online_retail
WHERE CustomerID IS NOT NULL AND Quantity > 0
GROUP BY StockCode, Description
ORDER BY TotalRevenue DESC
LIMIT 10;

-- 4. Cálculo del Modelo RFM Base (Recencia, Frecuencia y Monetario por Cliente)
SELECT 
    CustomerID,
    DATEDIFF('2011-12-09', MAX(InvoiceDate)) AS Recency,
    COUNT(DISTINCT InvoiceNo) AS Frequency,
    SUM(Quantity * UnitPrice) AS Monetary
FROM online_retail
WHERE CustomerID IS NOT NULL AND Quantity > 0
GROUP BY CustomerID;

-- 5. Países con Mayor Volumen de Ventas (Top Países fuera del mercado local principal)
SELECT 
    Country,
    SUM(Quantity * UnitPrice) AS TotalRevenue,
    COUNT(DISTINCT CustomerID) AS TotalCustomers
FROM online_retail
WHERE CustomerID IS NOT NULL AND Quantity > 0
GROUP BY Country
ORDER BY TotalRevenue DESC
LIMIT 5;