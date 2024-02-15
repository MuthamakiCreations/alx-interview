#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

if (!movieId || isNaN(movieId)) {
  console.error('Please provide a valid movie ID as the first argument.');
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Unexpected status code:', response.statusCode);
    process.exit(1);
  }

  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  if (!characters || characters.length === 0) {
    console.error('No characters found for this movie.');
    process.exit(1);
  }

  // Fetch character names
  const fetchCharacterNames = async () => {
    try {
      for (const characterUrl of characters) {
        const characterData = await fetchCharacterData(characterUrl);
        console.log(characterData.name);
      }
    } catch (error) {
      console.error('Error fetching character data:', error);
    }
  };

  const fetchCharacterData = (url) => {
    return new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          if (response.statusCode === 200) {
            resolve(JSON.parse(body));
          } else {
            reject(`Unexpected status code: ${response.statusCode}`);
          }
        }
      });
    });
  };

  // Start fetching character names
  fetchCharacterNames();
});