#!/usr/bin/node
if (!process.argv[2] || Number(process.argv[2]).isNaN === false) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < Number(process.argv[2]); i++) {
    console.log('C is fun');
  }
}
