#!/usr/bin/node

const request = require('request');
const filmEndpoint = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

function fetchCharacterName (url) {
  return request(url, (err, _, body) => {
    if (err) throw err;

    console.log(JSON.parse(body).name);
  });
}

request(filmEndpoint, (err, _, body) => {
  if (err) throw err;

  JSON.parse(body).characters.forEach(fetchCharacterName);
});
