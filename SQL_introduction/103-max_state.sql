-- Script that displays the max temperature of each state (ordered by State name).

-- Select each state and their max value
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state ASC;
