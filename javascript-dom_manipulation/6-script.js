// fetch Star Wars API and display character name in #character
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  // Convert response to json if ok
  .then((response) => {
    if (!response.ok) {
      throw new Error('Error while fetching character name');
    }

    return response.json();
  })
  // Extract name from json and display it in #character
  .then((json) => {
    document.querySelector('#character').innerHTML = json.name;
  })
  // Catch any error and display them in console
  .catch((error) => {
    console.error(error);
  });
