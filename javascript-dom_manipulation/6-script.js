fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then((response) => {
    if (!response.ok) {
      throw new Error('Error while fetching character name');
    }

    response.json()
      .then((character) => {
        document.querySelector('#character').innerHTML = character.name;
      });
  });
