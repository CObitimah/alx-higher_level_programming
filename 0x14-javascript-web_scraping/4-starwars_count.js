#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
const characterId = 18;
const characterUrl = `https://swapi-api.alx-tools.com/api/people/${characterId}/`;

if (!apiUrl) {
  console.error('Error: Missing API URL. Usage: ./4-starwars_count.js <api-url>');
  process.exit(1);
}

request.get(apiUrl, (err, response, body) => {
  if (err) {
    console.error(`Error making request: ${err.message}`);
    process.exit(1);
  } else if (response.statusCode !== 200) {
    console.error(`Error: Received status code ${response.statusCode}`);
    process.exit(1);
  } else {
    try {
      const films = JSON.parse(body).results;
      const wedgeCount = films.filter(film => film.characters.includes(characterUrl)).length;
      console.log(wedgeCount);
    } catch (parseError) {
      console.error(`Error parsing JSON: ${parseError.message}`);
      process.exit(1);
    }
  }
});
