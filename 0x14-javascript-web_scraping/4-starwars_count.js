#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./4-starwars_count.js <API URL>');
  process.exit(1);
}

const apiUrl = process.argv[2];
const wedgeAntillesId = '18';
let count = 0;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching data:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch data. Status code:', response.statusCode);
    return;
  }

  const films = JSON.parse(body).results;

  films.forEach(film => {
    if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeAntillesId}/`)) {
      count++;
    }
  });

  console.log(count);
});
