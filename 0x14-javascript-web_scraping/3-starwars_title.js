#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Error: Missing movie ID. Usage: node script.js <movie-id>');
  process.exit(1);
}

// Construct the API URL
const urlApi = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request.get(urlApi, (err, response, body) => {
  if (err) {
    console.error(`Error making request: ${err.message}`);
    process.exit(1);
  } 
  else if (response.statusCode !== 200) {
    console.error(`Error: Received status code ${response.statusCode}`);
    process.exit(1);
  } 
  else {
    try {
      const data = JSON.parse(body);
      console.log(data.title);
    } catch (parseError) {
      console.error(`Error parsing JSON: ${parseError.message}`);
      process.exit(1);
    }
  }
});
