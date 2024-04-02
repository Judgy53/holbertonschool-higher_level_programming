// Fetch Star Wars api and display all films in #list_movies
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  // Convert response to json if ok
  .then((response) => {
    if (!response.ok) {
      throw new Error('Error while fetching movie list');
    }

    return response.json();
  })
  // Extract film titles from json and display them in #list_movies
  .then((json) => {
    const listMovies = document.querySelector('#list_movies');
    json.results.forEach((film) => {
      const entry = document.createElement('li');
      entry.innerHTML = film.title;
      listMovies.append(entry);
    });
  })
  // Catch any error and display them in console
  .catch((error) => {
    console.error(error);
  });
