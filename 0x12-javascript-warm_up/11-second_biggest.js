#!/usr/bin/node
let argsCount = 0;
process.argv.forEach((element, index) => {
  argsCount++;
});
if (argsCount <= 3) {
  console.log('0');
} else {
  process.argv.sort((a, b) => a - b);
  console.log(process.argv[argsCount - 2]);
}
