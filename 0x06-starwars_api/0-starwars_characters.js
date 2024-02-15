#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const film = JSON.parse(body);
    const charactersUrls = film.characters;
    const promises = charactersUrls.map(url =>
      new Promise((resolve, reject) => {
        request(url, (error, response, body) => {
          if (error) {
            reject(error);
          } else {
            const character = JSON.parse(body);
            resolve(character.name);
          }
        });
      })
    );
    Promise.all(promises)
      .then(characters => {
        characters.forEach(character => console.log(character));
      })
      .catch(error => console.error('Error:', error));
  }
});
