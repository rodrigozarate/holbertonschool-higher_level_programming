#!/usr/bin/node
function factorialize (number) {
  let computed = 1;
  for (let i = 1; i <= number; i++) {
    computed *= i;
  }
  return (computed);
}
console.log(factorialize(parseInt(process.argv[2])));
