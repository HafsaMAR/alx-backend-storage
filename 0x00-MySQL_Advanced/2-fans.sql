--Data manipulation and agregation using sum
SOURCE metal_bands.sql

SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;