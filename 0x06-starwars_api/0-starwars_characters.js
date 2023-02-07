#!/usr/bin/node
const request = require('request');

const inputNum = process.argv;

const url = `https://swapi-api.alx-tools.com/api/films/${inputNum[2]}/`;

if (inputNum.length > 2) {
  request(url, function (err, response, body) {
    if (err) throw console.error(err);
    const charactersUrl = JSON.parse(body).characters;
    const charactersName = charactersUrl.map(
      url => new Promise((resolve, reject) => {
        request(url, (err, _, responseBody) => {
          if (err) {
            reject(err);
          }
          resolve(JSON.parse(responseBody).name);
        });
      })
    );
    Promise.all(charactersName)
      .then(names => console.log(names.join('\n')))
      .catch(allErrors => console.log(allErrors));
  });
}
