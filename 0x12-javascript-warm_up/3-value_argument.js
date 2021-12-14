#!/usr/bin/node
let argsCount = 0;
process.argv.forEach((element, index) => {
  argsCount++;
});
if (argsCount <= 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
