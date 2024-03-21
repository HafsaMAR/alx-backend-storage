-- Ading condition to the selection
-- calculating lifespan based on split year if not null
-- match any style that contains 'Glam rock' as a substring
SELECT band_name,
    CASE 
        WHEN split IS NULL THEN (2022 - formed)  
        ELSE  (split - formed)
    END AS lifespan
FROM metal_bands
WHERE style LIKE "%Glam rock%"
ORDER BY lifespan DESC;