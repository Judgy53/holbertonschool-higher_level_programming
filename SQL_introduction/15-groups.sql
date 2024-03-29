-- Script that lists the number of records with the same score in the table second_table

-- Query the score and the count of each one
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
