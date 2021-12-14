#!/usr/bin/node
const squareSize = parseInt(process.argv[2]);
let pattern = '';
if (squareSize) {
  for (let i = 0; i < squareSize; i++) {
    for (let j = 0; j < squareSize; j++) {
      pattern += 'X';
    }
    console.log(pattern);
  } else {
    console.log('Missing size');
}
