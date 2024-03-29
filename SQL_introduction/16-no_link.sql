-- Script that lists all records with a valid name of the table second_table

-- Query second_table for score and name where name is not null
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
