#!/usr/bin/node

const request = require('request');
const endpoint = process.argv[2];
const charId = '18';

/**
 * countAppearance - Add one to accumulator if character is in the film
 * @acc: Accumulator
 * @film: film data from api call.
 *
 * Return: new value for accumulator
 */
function countAppearance (acc, film) {
  if (film.characters.some((c) => c.indexOf(charId) > -1)) return acc + 1;
  return acc;
}

request(endpoint, (err, _, body) => {
  if (err) throw err;

  const json = JSON.parse(body);

  console.log(json.results.reduce(countAppearance, 0));
});
