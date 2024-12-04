-- Grouping sets
SELECT country, category, SUM(amount) AS "Total_sales"
FROM "FactSales"
LEFT JOIN "DimCountry"
ON "FactSales".countryid = "DimCountry".countryid
LEFT JOIN "DimCategory"
ON "FactSales".categoryid = "DimCategory".categoryid
GROUP BY GROUPING SETS(country, category)
ORDER BY country, category;

-- Roll up
SELECT "year", country, SUM(amount) AS "Total_sales"
FROM "FactSales"
LEFT JOIN "DimDate"
ON "FactSales".dateid = "DimDate".dateid
LEFT JOIN "DimCountry"
ON "FactSales".countryid = "DimCountry".countryid
GROUP BY ROLLUP ("year", country)
ORDER BY "year", country; 

-- Cube
SELECT "year", country, AVG(amount) AS "Total_sales"
FROM "FactSales"
LEFT JOIN "DimDate"
ON "FactSales".dateid = "DimDate".dateid
LEFT JOIN "DimCountry"
ON "FactSales".countryid = "DimCountry".countryid
GROUP BY CUBE ("year", country)
ORDER BY "year", country; 

-- MQT 
CREATE MATERIALIZED VIEW total_sales_per_country (country, Total_sales) As 
(SELECT country, SUM(amount) AS "Total_sales"
FROM "FactSales"
LEFT JOIN "DimCountry"
ON "FactSales".countryid = "DimCountry".countryid
GROUP BY country);