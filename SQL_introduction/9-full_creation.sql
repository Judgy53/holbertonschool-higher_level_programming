-- Script that creates a table called second_table in the current database in the MySQL server and inserts some records into it..

-- Create the table
CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	name VARCHAR(256),
	score INT
);

-- Insert records for John, Alex, Bob and George
INSERT INTO second_table (id, name, score) 
	VALUES(1, "John", 10), (2, "Alex", 3), (3, "Bob", 14), (4, "George", 8);
