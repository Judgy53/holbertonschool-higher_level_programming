fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then((response) => {
    if (!response.ok) {
      throw new Error('Error while fetching movie list');
    }

    response.json()
      .then((films) => {
        const listMovies = document.querySelector('#list_movies');
        films.results.forEach((f) => {
          const entry = document.createElement('li');
          entry.innerHTML = f.title;
          listMovies.append(entry);
        });
      });
  });
