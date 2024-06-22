#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./100-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching data:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch data. Status code:', response.statusCode);
    return;
  }

  const filmData = JSON.parse(body);
  const charactersUrls = filmData.characters;

  // Function to fetch character name from URL
  const fetchCharacterName = (url) => {
    return new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          const characterData = JSON.parse(body);
          resolve(characterData.name);
        }
      });
    });
  };

  // Array to store promises of character names
  const promises = charactersUrls.map(characterUrl => fetchCharacterName(characterUrl));

  // Resolve all promises and print character names
  Promise.all(promises)
    .then(names => {
      names.forEach(name => console.log(name));
    })
    .catch(error => {
      console.error('Error fetching character:', error);
    });
});
