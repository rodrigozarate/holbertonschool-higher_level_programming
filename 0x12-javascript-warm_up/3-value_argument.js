#!/usr/bin/node
let givenArg = 'No argument'
let argsCount = 0;
process.argv.forEach((element, index) => {
  argsCount++;
});
if (argsCount <= 2) {
  console.log(givenArg);
} else {
  console.log(process.argv[2]);
}
