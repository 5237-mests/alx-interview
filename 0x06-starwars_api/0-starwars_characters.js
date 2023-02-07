#!/usr/bin/node
const request = require('request');
const process = require('process');

const inputNum = process.argv;

const url = `https://swapi-api.alx-tools.com/api/films/${inputNum[2]}/`;

request(url, function (err, response, body) {
  if (err) throw console.error(err);
  const newbody = JSON.parse(body);
  const people = newbody.characters;
  for (const actor of people) {
    request(actor, function (err, res, body2) {
      if (err) throw console.error(err);
      const newbody2 = JSON.parse(body2);
      console.log(newbody2.name);
    });
  }
});
