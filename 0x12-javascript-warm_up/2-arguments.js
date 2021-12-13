#!/usr/bin/node
let argsCount = 0;
process.argv.forEach((_val, _index) => {
  argsCount++;
});
if (argsCount <= 2) {
  console.log('No argument');
} else if (argsCount === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
