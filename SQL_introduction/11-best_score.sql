-- Script that lists all records with a score >= 10 in the table second_table of the current database, ordered by score

-- Select score and name from records where score >=10 and order by score (bigger first)
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC
