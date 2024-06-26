-- Script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)

-- Select top 3 city and their average temperature
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month BETWEEN 7 AND 8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
