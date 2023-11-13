#!/usr/bin/node
const argNum = parseInt(process.argv[2]);

if (Number.isNaN(argNum)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < argNum; i++) {
    let row = '';
    for (let j = 0; j < argNum; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
