# SQL_introduction
Project in SQL to learn basic syntax, how to create and modify a database, and how to query from it.

## 0-list_databases.sql - List databases 
Script that lists all databases of your MySQL server.
	
## 1-create_database_if_missing.sql - Create a database 
Script that creates the database `hbtn_0c_0`.
- If the database `hbtn_0c_0` already exists, the script should not fail
	
## 2-remove_database.sql - Delete a database 
Script that deletes the database `hbtn_0c_0`.
- If the database `hbtn_0c_0` doesn’t exist, the script should not fail
	
## 3-list_tables.sql - List tables 
Script that lists all the tables of a database.
- The database name needs to be passed as argument of mysql command
	
## 4-first_table.sql - First table 
Script that creates a table called `first_table` in the current database.
- The database name needs to be passed as an argument of the mysql command
- `first_table` description:
  - `id` INT
  - `name` VARCHAR(256)
- If the table first_table already exists, your script should not fail
	
## 5-full_table.sql - Full description 
Script that prints the full description of the table `first_table` from the current database.
- The database name needs to be passed as an argument of the mysql command
	
## 6-list_values.sql - List all in table 
Script that lists all rows of the table `first_table` from the current database.
- The database name needs to be passed as an argument of the mysql command
- All fields should be printed
	
## 7-insert_value.sql - First add
Script that inserts a new row in the table `first_table`.
- The database name needs be passed as an argument of the mysql command
- New row:
  - `id` = 89
  - `name` = Best School
	
## 8-count_89.sql - Count 89 
Script that displays the number of records with `id` = 89 in the table `first_table`.
- The database name needs be passed as an argument of the mysql command
	
## 9-full_creation.sql - Full creation 
Script that creates a table `second_table` in the current database and add multiples rows.
- The database name needs be passed as an argument of the mysql command
- `second_table` description:
  - `id` INT
  - `name` VARCHAR(256)
  - `score` INT
- If the table second_table already exists, your script should not fail
- The script should create these records:
  - `id` = 1, `name` = “John”, `score` = 10
  - `id` = 2, `name` = “Alex”, `score` = 3
  - `id` = 3, `name` = “Bob”, `score` = 14
  - `id` = 4, `name` = “George”, `score` = 8
	
## 10-top_score.sql - List by best 
Script that lists all records of the table `second_table`.
- The database name needs be passed as an argument of the mysql command
- Results should display both the score and the name (in this order)
- Records should be ordered by score (top first) 

## 11-best_score.sql - Select the best 
Script that lists all records with a `score >= 10` in the table `second_table`.
- The database name needs be passed as an argument of the mysql command
- Results should display both the score and the name (in this order)
- Records should be ordered by score (top first)
	
## 12-no_cheating.sql - Cheating is bad 
Script that updates the score of Bob to 10 in the table `second_table`.
- The database name needs be passed as an argument of the mysql command
	
## 13-change_class.sql - Score too low
Script that removes all records with a score <= 5 in the table `second_table`
- The database name needs be passed as an argument of the mysql command
	
## 14-average.sql - Average 
Script that computes the score average of all records in the table `second_table`
- The database name needs be passed as an argument of the mysql command
- The result column name should be `average`
	
## 15-groups.sql - Number by score 
Script that lists the number of records with the same score in the table `second_table`
- The database name needs be passed as an argument of the mysql command
- The result should display:
  - the score
  - the number of records for this score with the label `number`
- The list should be sorted by the number of records (descending)
	
## 16-no_link.sql - Say my name 
Script that lists all records of the table `second_table`
- The database name needs be passed as an argument of the mysql command
- Don’t list rows without a name value
- Results should display the score and the name (in this order)
- Records should be listed by descending score 

## 100-move_to_utf8.sql - Go to UTF8
Script that converts `hbtn_0c_0` database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
- You need to convert all of the following to UTF8:
  - Database `hbtn_0c_0`
  - Table `first_table`
  - Field `name` in first_table

	
## 101-avg_temperatures.sql - Temperatures #0 
Script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
- Import in `hbtn_0c_0` database this table dump: [download](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/272/temperatures.sql)
	
## 102-top_city.sql - Temperatures #1 
Script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)
- Import in `hbtn_0c_0` database this table dump (same as 101): [download](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/272/temperatures.sql)
	
## 103-max_state.sql - Temperatures #2 
Script that displays the max temperature of each state (ordered by State name).
- Import in `hbtn_0c_0` database this table dump (same as 101): [download](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/272/temperatures.sql)
