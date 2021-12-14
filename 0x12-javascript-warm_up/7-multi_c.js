#!/usr/bin/node
if (parseInt(process.argv[2])) {
  for (let x = 0; x < parseInt(process.argv[2]); x++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
