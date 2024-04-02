# javascript-web_scraping
Project in Javascript to learn how to use nodejs to interact with the system, and to use request to fetch data from the internet.

## 0-readme.js - Readme
Script that reads and prints the content of a file.
- The first argument is the file path
- The content of the file is read in utf-8
	
## 1-writeme.js - Write me
Script that writes a string to a file.
- The first argument is the file path
- The second argument is the string to write
- The content of the file is written in utf-8
	
## 2-statuscode.js - Status code
Script that display the status code of a GET request using module `request`.
- The first argument is the URL to request (GET)
- The status code is printed like this: `code: <status code>`
	
## 3-starwars_title.js - Star wars movie title 
Script that prints the title of a Star Wars movie where the episode number matches a given integer.
- The first argument is the movie ID
- Title is fetch on the Star wars API with the endpoint https://swapi-api.hbtn.io/api/films/:id
	
## 4-starwars_count.js - Star wars Wedge Antilles
Script that prints the number of movies where the character “Wedge Antilles” is present.
- The first argument is the API URL of the Star wars API: https://swapi-api.hbtn.io/api/films/
- Wedge Antilles is character ID 18 - the script use this ID for filtering the result of the API
	
## 5-request_store.js - Loripsum
Script that gets the contents of a webpage and stores it in a file.
- The first argument is the URL to request
- The second argument the file path to store the body response
- The file will be UTF-8 encoded
	
## 6-completed_tasks.js - How many completed?
Script that computes the number of tasks completed by user id.
- The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
- Only prints users with at least 1 completed task

## 100-starwars_characters.js - Who was playing in this movie? 
Script that prints all characters of a Star Wars movie:
- The first argument is the Movie ID - example: 3 = “Return of the Jedi”
- Display one character name by line
- Uses the Star wars API: https://swapi-api.hbtn.io/api/
	
## 101-starwars_characters.js
Script that prints all characters of a Star Wars movie:
- The first argument is the Movie ID - example: 3 = “Return of the Jedi”
- Display one character name by line **in the same order of the list** “characters” in the /films/ response
- Uses the Star wars API: https://swapi-api.hbtn.io/api/
