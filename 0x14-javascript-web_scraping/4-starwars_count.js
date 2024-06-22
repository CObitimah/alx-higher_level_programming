#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./4-starwars_count.js <API URL>');
  process.exit(1);
}

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching data:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch data. Status code:', response.statusCode);
    return;
  }

  try {
    const data = JSON.parse(body);
    const films = data.results;
    const wedgeAntillesUrl = 'https://swapi-api.alx-tools.com/api/people/18/';
    let count = 0;

    films.forEach(film => {
      if (film.characters.includes(wedgeAntillesUrl)) {
        count++;
      }
    });

    console.log(count);
  } catch (e) {
    console.error('Error parsing JSON:', e.message);
  }
});
